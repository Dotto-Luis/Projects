#!/usr/bin/env python3
"""
Casitas LLM Scoring Pipeline
Evaluates properties using Ollama (local LLM) + Buy Box criteria
"""

import os
import sys
import json
import time
import glob
import logging
from datetime import datetime
from pathlib import Path

import pandas as pd
import ollama

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURATION
# ─────────────────────────────────────────────────────────────────────────────

PROJECT_ROOT = Path(__file__).parent.parent
BUY_BOX_PATH = PROJECT_ROOT / "config" / "buy_box_malaga_2026.md"
INPUT_PATTERN = str(PROJECT_ROOT / "data" / "processed" / "activos_*.csv")
OUTPUT_DIR = PROJECT_ROOT / "data" / "output"

MODEL_NAME = "mistral"
BATCH_SIZE = 5

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s — %(levelname)s — %(message)s"
)
logger = logging.getLogger(__name__)

# Required columns (Spanish names, produced by the scrapers)
REQUIRED_COLUMNS = [
    "url", "titulo", "ubicacion", "precio", "m2",
    "habitaciones", "baños", "planta", "ascensor",
    "tipo", "estado", "año", "comentario", "plataforma",
]

# ─────────────────────────────────────────────────────────────────────────────
# SETUP (called from main() — kept out of import time so the module can be
# imported and unit-tested without Ollama, config files or data present)
# ─────────────────────────────────────────────────────────────────────────────


def load_buy_box(path: Path = BUY_BOX_PATH) -> str:
    """Read the Buy Box investment criteria document."""
    if not path.exists():
        raise FileNotFoundError(f"Buy Box not found: {path}")
    buy_box = path.read_text(encoding="utf-8")
    logger.info(f"Buy Box loaded from {path}")
    return buy_box


def verify_ollama(model_name: str = MODEL_NAME) -> None:
    """Fail fast with a clear message if the local LLM is not reachable."""
    try:
        models = ollama.list()
        available = [m.model for m in models.models] if hasattr(models, "models") else []
        logger.info(f"Ollama available. Models: {available[:3]}")
        if model_name not in available:
            logger.warning(f"Model '{model_name}' not found locally.")
            logger.info(f"Will attempt to pull: ollama pull {model_name}")
    except Exception as e:
        raise RuntimeError(
            f"Ollama not running or not available: {e}. "
            "Ensure Ollama is installed and running: ollama serve"
        ) from e


def load_latest_dataset(pattern: str = INPUT_PATTERN) -> pd.DataFrame:
    """Load the most recent processed dataset and validate its schema."""
    files = sorted(glob.glob(pattern))
    if not files:
        raise FileNotFoundError(f"No files matching pattern: {pattern}")

    input_file = files[-1]
    df = pd.read_csv(input_file)
    logger.info(f"File loaded: {input_file}")
    logger.info(f"Properties to evaluate: {len(df)}")

    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    return df


# ─────────────────────────────────────────────────────────────────────────────
# SCORING FUNCTIONS
# ─────────────────────────────────────────────────────────────────────────────

def clean_json(text: str) -> str:
    """Extract valid JSON from LLM response."""
    start = text.find("{")
    end = text.rfind("}") + 1

    if start == -1 or end == 0:
        raise ValueError("No JSON found in response")

    json_str = text[start:end]
    json_str = json_str.replace("True", "true").replace("False", "false").replace("None", "null")

    return json_str


def normalize_recommendation(value) -> str:
    """Standardize recommendation values."""
    if pd.isna(value):
        return "error"

    value = str(value).lower().strip()
    mapping = {
        "discard": "discard",
        "discarded": "discard",
        "worth_visit": "worth_visit",
        "visit": "worth_visit",
        "opportunity": "strong_opportunity",
        "strong_opportunity": "strong_opportunity",
        "price_only": "price_only",
    }
    return mapping.get(value, value)


def clamp_score(score) -> float:
    """Ensure score is between 0 and 100."""
    try:
        score = float(score)
        return max(0, min(100, score))
    except:
        return None


def build_prompt(prop: dict, buy_box: str | None = None) -> str:
    """Compose the scoring prompt for one property.

    If `buy_box` is provided, the full investment-criteria document is injected
    into the context so the LLM scores against the real zone/price/condition
    thresholds instead of the generic tiers below.
    """
    criteria_block = (
        f"\nINVESTMENT CRITERIA (Buy Box — score against these):\n{buy_box}\n"
        if buy_box
        else ""
    )

    return f"""Analyze this Málaga real estate investment and score it.

PROPERTY DATA:
Title: {str(prop.get('titulo', 'N/A'))[:60]}
Price: €{prop.get('precio', 'N/A')}
Size: {prop.get('m2', 'N/A')}m²
Beds/Baths: {prop.get('habitaciones', 'N/A')}/{prop.get('baños', 'N/A')}
Location: {prop.get('ubicacion', 'N/A')}
Condition: {prop.get('estado', 'N/A')}
Year: {prop.get('año', 'N/A')}
Elevator: {prop.get('ascensor', 'N/A')}
{criteria_block}
SCORING CRITERIA (0-100):
- 85-100: Strong opportunity (good value, strong fundamentals)
- 70-84: Worth visiting (decent potential, standard market)
- 60-69: Only if excellent price (marginal, needs negotiation)
- <60: Discard (poor fundamentals, high risk)

VALID RECOMMENDATIONS:
- "opportunity" for score 85-100
- "visit" for score 70-84
- "price" for score 60-69
- "discard" for score <60

Analyze carefully and return ONLY valid JSON with integer score (0-100) and recommendation:
{{"score": <your_score>, "rec": "<your_rec>"}}"""


def score_property(prop: dict, buy_box: str | None = None) -> dict:
    """
    Evaluate a property using Ollama (local LLM) with clear scoring criteria.

    `buy_box`: pass the Buy Box document to score against the real criteria.
    Left as None reproduces the original behaviour (generic tiers only).
    """
    prompt = build_prompt(prop, buy_box)

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    raw_response = response["message"]["content"]

    try:
        json_str = clean_json(raw_response)
        result = json.loads(json_str)

        if "score" in result and "score_total" not in result:
            result["score_total"] = result.get("score", 50)
        if "rec" in result and "recommendation" not in result:
            rec_raw = str(result.get("rec", "visit")).lower().strip()
            rec_map = {
                "opportunity": "strong_opportunity",
                "visit": "worth_visit",
                "discard": "discard",
                "discarded": "discard",
                "price": "price_only"
            }
            result["recommendation"] = rec_map.get(rec_raw, "worth_visit")

    except Exception as e:
        result = {
            "score_total": 0,
            "recommendation": "discard",
        }

    result.setdefault("score_total", 50)
    result.setdefault("recommendation", "worth_visit")
    result.setdefault("rationale", "")

    result["url"] = prop.get("url")
    result["titulo"] = prop.get("titulo")
    result["ubicacion"] = prop.get("ubicacion")
    result["precio"] = prop.get("precio")
    result["m2"] = prop.get("m2")
    result["habitaciones"] = prop.get("habitaciones")
    result["baños"] = prop.get("baños")
    result["planta"] = prop.get("planta")
    result["ascensor"] = prop.get("ascensor")
    result["plataforma"] = prop.get("plataforma")
    result["tipo"] = prop.get("tipo")
    result["estado"] = prop.get("estado")
    result["año"] = prop.get("año")

    return result


# ─────────────────────────────────────────────────────────────────────────────
# MAIN SCORING LOOP
# ─────────────────────────────────────────────────────────────────────────────

def main():
    # Setup: config, LLM availability and data — each fails with a clear message
    try:
        load_buy_box()
        verify_ollama()
        df = load_latest_dataset()
    except (FileNotFoundError, RuntimeError, ValueError) as e:
        logger.error(str(e))
        sys.exit(1)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    results = []
    errors = []

    timestamp = datetime.now().strftime("%Y%m%d_%H%M")

    logger.info(f"Starting scoring loop for {len(df)} properties...")
    start_time = time.time()

    for idx, (i, row) in enumerate(df.iterrows()):
        prop = row.to_dict()
        title = str(prop.get('title', ''))[:60]

        logger.info(f"[{idx+1}/{len(df)}] {title}...")

        try:
            result = score_property(prop)

            result["url"] = prop.get("url")
            result["titulo"] = prop.get("titulo")
            result["ubicacion"] = prop.get("ubicacion")
            result["precio"] = prop.get("precio")
            result["m2"] = prop.get("m2")
            result["habitaciones"] = prop.get("habitaciones")
            result["baños"] = prop.get("baños")
            result["planta"] = prop.get("planta")
            result["ascensor"] = prop.get("ascensor")
            result["plataforma"] = prop.get("plataforma")
            result["tipo"] = prop.get("tipo")
            result["estado"] = prop.get("estado")
            result["año"] = prop.get("año")

            result["score_total"] = clamp_score(result.get("score_total"))
            result["recommendation"] = normalize_recommendation(result.get("recommendation"))

            results.append(result)

            logger.info(f"Score: {result['score_total']} — {result['recommendation']}")

        except json.JSONDecodeError as e:
            logger.error(f"JSON Parse Error: {e}")
            errors.append({
                "url": prop.get("url"),
                "title": prop.get("title"),
                "error": f"JSON Parse: {str(e)}"
            })
            results.append({
                "url": prop.get("url"),
                "title": prop.get("title"),
                "score_total": 0,
                "recommendation": "discard",
                "rationale": str(e)
            })
        except Exception as e:
            logger.error(f"Error: {e}")
            errors.append({
                "url": prop.get("url"),
                "title": prop.get("title"),
                "error": str(e)
            })
            results.append({
                "url": prop.get("url"),
                "title": prop.get("title"),
                "score_total": 0,
                "recommendation": "discard",
                "rationale": f"Error: {str(e)}"
            })

        if (idx + 1) % BATCH_SIZE == 0:
            logger.info(f"Checkpoint: {idx + 1}/{len(df)} saved")

        time.sleep(1)

    # ─────────────────────────────────────────────────────────────────────────
    # SAVE RESULTS
    # ─────────────────────────────────────────────────────────────────────────

    df_scoring = pd.DataFrame(results)
    df_errors = pd.DataFrame(errors) if errors else pd.DataFrame()

    df_scoring["recommendation"] = df_scoring["recommendation"].apply(normalize_recommendation)
    df_scoring["score_total"] = df_scoring["score_total"].apply(clamp_score)
    df_scoring = df_scoring.sort_values("score_total", ascending=False, na_position="last")

    ranking_path = OUTPUT_DIR / f"ranking_final_{timestamp}.csv"
    df_scoring.to_csv(ranking_path, index=False)

    logger.info(f"Ranking saved: {ranking_path}")

    if not df_errors.empty:
        errors_path = OUTPUT_DIR / f"scoring_errors_{timestamp}.csv"
        df_errors.to_csv(errors_path, index=False)
        logger.info(f"Errors saved: {errors_path}")

    # ─────────────────────────────────────────────────────────────────────────
    # SUMMARY REPORT
    # ─────────────────────────────────────────────────────────────────────────

    elapsed = time.time() - start_time

    print("\n" + "=" * 70)
    print("SCORING COMPLETE — CASITAS MALAGA 2026")
    print("=" * 70)
    print(f"Properties scored:        {len(df_scoring)}")
    print(f"Errors:                   {len(df_errors)}")
    print(f"Time elapsed:             {elapsed:.1f}s ({elapsed/len(df):.2f}s/property)")

    print(f"\nRecommendations:")
    print(df_scoring["recommendation"].value_counts(dropna=False).to_string())

    print(f"\nScore distribution:")
    print(df_scoring["score_total"].describe().to_string())

    print(f"\nTop 10 Properties:")
    top_cols = ["titulo", "ubicacion", "precio", "m2", "score_total", "recommendation", "plataforma"]
    print(df_scoring[top_cols].head(10).to_string(index=False))

    print("=" * 70)
    print(f"Ranking file: {ranking_path}")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
