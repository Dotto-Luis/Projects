import re
import pandas as pd
from scrapers.config import LINKS_PATH

DOMINIOS = [
    "idealista", "fotocasa", "pisos.com",
    "yaencontre", "tecnocasa", "habitaclia"
]

def es_valido(url):
    url = str(url).lower()
    if "obra-nueva" in url: return False
    if "terreno" in url: return False
    if "alquilar" in url or "alquiler" in url: return False
    return True

def extraer_links_chat(ruta_chat):
    with open(ruta_chat, "r", encoding="utf-8") as f:
        texto = f.read()

    patron = r'https?://[^\s\]>)"]+'
    todos = re.findall(patron, texto)

    inmobiliarios = [
        url for url in todos
        if any(d in url for d in DOMINIOS) and es_valido(url)
    ]

    return list(dict.fromkeys(inmobiliarios))

def actualizar_links(ruta_chat):
    links_chat = extraer_links_chat(ruta_chat)
    print(f"Links válidos extraídos del chat: {len(links_chat)}")

    # Cargar existentes
    df_existentes = pd.read_csv(LINKS_PATH, header=0)
    df_existentes.columns = ["url", "extra"]
    urls_existentes = set(df_existentes["url"].str.strip().tolist())

    # Filtrar nuevos
    nuevos = [u for u in links_chat if u not in urls_existentes]
    print(f"Links nuevos a agregar: {len(nuevos)}")

    if not nuevos:
        print("✅ No hay links nuevos")
        return

    df_nuevos = pd.DataFrame({"url": nuevos, "extra": ""})
    df_actualizado = pd.concat([df_existentes, df_nuevos], ignore_index=True)
    df_actualizado.to_csv(LINKS_PATH, index=False, header=False)

    print(f"✅ links_viviendas.csv actualizado — total: {len(df_actualizado)}")
    for url in nuevos:
        print(f"  + {url}")