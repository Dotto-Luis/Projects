import random
from datetime import datetime
from pathlib import Path

import pandas as pd
import undetected_chromedriver as uc

from scrapers.config import PROJECT_ROOT, RAW_DIR, LINKS_PATH, WAIT_LONG_EVERY
from scrapers.utils import cargar_links, esperar_entre_requests, esperar_pausa_larga
from scrapers.idealista import scrape_idealista
from scrapers.fotocasa import scrape_fotocasa
from scrapers.pisoscom import scrape_pisos
from scrapers.yaencontre import scrape_yaencontre
from scrapers.tecnocasa import scrape_tecnocasa
from scrapers.config import PROJECT_ROOT
from scrapers.whatsapp_extractor import actualizar_links

# ── PATHS ────────────────────────────────────────────
LOG_DIR = PROJECT_ROOT / "data" / "logs"
SCRAPE_LOG_PATH = LOG_DIR / "scrape_log.csv"
LATEST_SNAPSHOT_PATH = LOG_DIR / "latest_snapshot.csv"
PRICE_HISTORY_PATH = LOG_DIR / "price_history.csv"

# ── SCRAPERS ─────────────────────────────────────────
SCRAPERS = {
    "idealista":  scrape_idealista,
    "fotocasa":   scrape_fotocasa,
    "pisos":      scrape_pisos,
    "yaencontre": scrape_yaencontre,
    "tecnocasa":  scrape_tecnocasa,
}

# ── HELPERS ──────────────────────────────────────────
def load_csv_if_exists(path):
    if Path(path).exists():
        return pd.read_csv(path)
    return pd.DataFrame()


def get_pending_urls(urls, platform_name):
    latest = load_csv_if_exists(LATEST_SNAPSHOT_PATH)
    if latest.empty:
        return urls
    already_scraped = set(
        latest[latest["plataforma"] == platform_name]["url"]
    )
    return [url for url in urls if url not in already_scraped]


def update_tracking_files(resultados, platform_name, timestamp):
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    df_new = pd.DataFrame(resultados)
    if df_new.empty:
        return

    df_new["scraped_at"] = timestamp

    # ── Scrape log ───────────────────────────────────
    log_cols = ["url", "plataforma", "estado_anuncio", "scraped_at"]
    df_log_new = df_new[log_cols].copy()
    df_log_new["status"] = "success"
    old_log = load_csv_if_exists(SCRAPE_LOG_PATH)
    pd.concat([old_log, df_log_new], ignore_index=True).to_csv(
        SCRAPE_LOG_PATH, index=False
    )

    # ── Latest snapshot ──────────────────────────────
    old_snapshot = load_csv_if_exists(LATEST_SNAPSHOT_PATH)
    combined = pd.concat([old_snapshot, df_new], ignore_index=True)
    combined = combined.sort_values("scraped_at")
    latest = combined.drop_duplicates(subset=["url"], keep="last")
    latest.to_csv(LATEST_SNAPSHOT_PATH, index=False)

    # ── Price history ────────────────────────────────
    if not old_snapshot.empty and "precio" in old_snapshot.columns:
        previous = old_snapshot[["url", "precio"]].rename(
            columns={"precio": "precio_anterior"}
        )
        comparison = df_new.merge(previous, on="url", how="left")
        changed = comparison[
            comparison["precio"].notna() &
            comparison["precio_anterior"].notna() &
            (comparison["precio"] != comparison["precio_anterior"])
        ].copy()

        if not changed.empty:
            changed["price_change"] = changed["precio"] - changed["precio_anterior"]
            changed["price_change_pct"] = changed["price_change"] / changed["precio_anterior"]

            old_history = load_csv_if_exists(PRICE_HISTORY_PATH)
            history_cols = [
                "url", "plataforma", "scraped_at",
                "precio_anterior", "precio",
                "price_change", "price_change_pct", "estado_anuncio"
            ]
            pd.concat(
                [old_history, changed[history_cols]],
                ignore_index=True
            ).to_csv(PRICE_HISTORY_PATH, index=False)

            print(f"💰 {len(changed)} cambios de precio detectados")


def run_scraper(driver, urls, scraper_func, platform_name, timestamp):
    resultados = []

    for i, url in enumerate(urls):
        print(f"\nScraping {platform_name} {i+1}/{len(urls)}: {url[:60]}")
        try:
            piso = scraper_func(driver, url)
            resultados.append(piso)
            print(f"✓ {piso['estado_anuncio']} — {piso['titulo']} — {piso['precio']}€")
        except Exception as e:
            print(f"✗ Error: {e}")

        esperar_entre_requests()

        if (i + 1) % random.randint(*WAIT_LONG_EVERY) == 0:
            print("Pausa larga...")
            esperar_pausa_larga()

    df = pd.DataFrame(resultados)
    output_path = RAW_DIR / f"{platform_name}_scraped_{timestamp}.csv"
    df.to_csv(output_path, index=False)
    print(f"\n✅ {platform_name} — {len(resultados)} pisos → {output_path}")

    if not df.empty and "estado_anuncio" in df.columns:
        print(df["estado_anuncio"].value_counts())

    update_tracking_files(resultados, platform_name, timestamp)
    return df


# ── MAIN ─────────────────────────────────────────────
def main():
        # ── Actualizar links desde WhatsApp ──────────────
    chat_path = PROJECT_ROOT / "data" / "raw" / "_chat.txt"
    if chat_path.exists():
        print("📱 Actualizando links desde WhatsApp...")
        actualizar_links(chat_path)
    else:
        print("⚠️ No hay _chat.txt — saltando extracción WhatsApp")
    
    PROJECT_ROOT.mkdir(parents=True, exist_ok=True)
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    df_links, listas = cargar_links(LINKS_PATH)

    print(f"Total links: {len(df_links)}")
    for plataforma, urls in listas.items():
        print(f"  {plataforma}: {len(urls)}")

    driver = uc.Chrome(version_main=148)
    print("\nDriver iniciado")

    try:
        for plataforma, scraper_func in SCRAPERS.items():
            urls = listas.get(plataforma, [])
            if not urls:
                print(f"\n⏭ {plataforma} — sin links")
                continue

            pending = get_pending_urls(urls, plataforma)
            print(f"\n{'='*50}")
            print(f"{plataforma}: {len(urls)} total | {len(pending)} pendientes")

            if not pending:
                print(f"✅ Todo ya scrapeado")
                continue

            run_scraper(
                driver=driver,
                urls=pending,
                scraper_func=scraper_func,
                platform_name=plataforma,
                timestamp=timestamp,
            )

    finally:
        driver.quit()
        print("\n✅ Driver cerrado")
        print(f"\nLogs en: {LOG_DIR}")


if __name__ == "__main__":
    main()