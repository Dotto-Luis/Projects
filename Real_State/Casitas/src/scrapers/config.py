from pathlib import Path

# Resolved relative to this file (src/scrapers/config.py -> project root),
# so the project works from any clone location.
PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"

LINKS_PATH = RAW_DIR / "links_viviendas.csv"

SOURCES = {
    "idealista": "idealista",
    "fotocasa": "fotocasa",
    "pisos": "pisos.com",
    "habitaclia": "habitaclia",
    "tecnocasa": "tecnocasa",
    "yaencontre": "yaencontre",
}

WAIT_PAGE_LOAD = (5, 9)
WAIT_MIN = 4
WAIT_MAX = 15
WAIT_LONG = (25, 45)
WAIT_LONG_EVERY = (8, 12)