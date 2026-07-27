# Casitas Architecture & Technical Documentation

## System Overview

Casitas is a multi-stage ETL (Extract, Transform, Load) + LLM pipeline that automates real estate investment analysis.

```
┌─────────────────────────────────────────────────────────────────────┐
│                      CASITAS PIPELINE v1.1                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  STAGE 1: SCRAPE        STAGE 2: CLEAN      STAGE 3: SCORE       │
│  ─────────────────      ──────────────      ─────────────        │
│  7 web sources    →     Deduplicate   →     Claude/Ollama  →     │
│  (73+ properties)       (136 active)        (LLM scoring)         │
│                                                                     │
│  Output: raw/*.csv      processed/*.csv     output/ranking*.csv   │
│                                             output/entrega*.csv   │
│                                             output/*.png          │
│                         STAGE 4: REPORT                           │
│                         ───────────────                           │
│                         Merge + Charts                            │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Stage 1: Web Scraping

**File:** `notebooks/01_scraper.ipynb`

### Architecture

```
Input: data/raw/links_viviendas.csv (191 URLs)
         ↓
    Undetected ChromeDriver
         ↓
    Per-platform scrapers (6 implementations)
         ↓
    Output: data/raw/*_scraped_*.csv (11 files)
```

### Platform Adapters

Each platform has unique HTML structure; individual parsers handle detection:

| Platform | Scraper | Key Classes | Sample Output |
|----------|---------|-------------|---------------|
| Idealista | `scrapers/idealista.py` | `.info-data-price`, `.main-info__title-main` | titulo, precio, m2 |
| Fotocasa | `scrapers/fotocasa.py` | `.re-DetailHeader-price`, `.re-ContentDetail-topContainer--main` | + ascensor, features |
| Pisos.com | `scrapers/pisoscom.py` | `.price__value`, `.features-summary` | + planta, condition |
| YaEncontre | `scrapers/yaencontre.py` | `.details-header-info` (JS extract) | +year, año |
| Tecnocasa | `scrapers/tecnocasa.py` | `.current-price`, `.estate-features` | + anunciante |
| Habitaclia | ❌ Not yet implemented | - | - |

### Anti-Detection Measures

```python
import undetected_chromedriver as uc
driver = uc.Chrome()  # Bypasses CloudFlare/bot detection

# Human-like timing
WAIT_PAGE_LOAD = (5, 9)      # 5-9 sec per page
WAIT_MIN = 4, WAIT_MAX = 15  # 4-15 sec between requests
WAIT_LONG = (25, 45)          # Occasional 25-45 sec pause
```

### Data Schema (Output)

```python
{
    "url": "https://...",
    "plataforma": "idealista",
    "estado_anuncio": "activo" | "dado de baja",
    "titulo": str,
    "ubicacion": str,
    "precio": int,              # €
    "m2": int,
    "habitaciones": int,
    "baños": int,
    "planta": str,              # "3ª planta" or "ground floor"
    "ascensor": "Sí" | "No" | None,
    "tipo": "Piso" | "Casa" | "Ático",
    "estado": "Buen estado" | "Reformado" | "Nuevo" | None,
    "año": int,                 # Construction year
    "anunciante": str,          # Agent/seller name
    "comentario": str           # Full property description
}
```

### Challenges Overcome

1. **JavaScript-heavy pages (YaEncontre):**
   - Solution: Use Selenium `execute_script()` to extract data post-JS-render
   
2. **Rate limiting (Idealista, Tecnocasa):**
   - Solution: Random 15-45s pauses between request batches
   
3. **Different HTML per site:**
   - Solution: Fallback parsing (try primary selector, then alternates)
   - Example: Try `.re-DetailHeader-price` → `.main-price` → regex on page text

---

## Stage 2: Data Cleaning & Analysis

**File:** `notebooks/02_analisis.ipynb`  
**Technology:** DuckDB (in-process SQL)

### ETL Flow

```python
# 1. Load all raw CSVs
viviendas_raw = read_csv_auto('data/raw/*_scraped_*.csv')
# Result: 297 records across 11 files

# 2. Deduplicate by URL
viviendas_limpias = SELECT * FROM viviendas_raw 
    WHERE rn = 1 OVER (PARTITION BY url ORDER BY date DESC)
# Result: 188 unique URLs (52 duplicates removed)

# 3. Filter active listings
viviendas_activas = SELECT * FROM viviendas_limpias
    WHERE estado_anuncio = 'activo'
# Result: 136 active properties

# 4. Type conversion
precio → Int64
m2 → Int64
habitaciones → Int64
año → Int64

# 5. Detect situation (free/rented/occupied/disputed)
situacion = detectar_situacion(comentario, titulo)
# Output: 125 libre, 4 alquilado, 3 local, 2 ocupado, 1 subasta, 1 nuda propiedad
```

### Quality Metrics

```
Input:  297 records
├── Duplicates removed:     52 (-17.5%)
├── Inactive filtered:      45 (-15.2%)
└── Output:                136 (45.8% retention)

Data Completeness (136 active properties):
├── precio:       110/136 filled (80.9%)
├── m2:           106/136 filled (77.9%)
├── habitaciones:  98/136 filled (72.1%)
├── baños:         100/136 filled (73.5%)
├── año:            42/136 filled (30.9%)
└── comentario:    135/136 filled (99.3%)
```

### Data Quality Issues

| Issue | Count | Impact | Solution |
|-------|-------|--------|----------|
| Missing m² | 30 | Yield calculation error | Fallback to avg for zone |
| Missing year | 94 | Age scoring = 0 | Infer from description |
| m² > 300 | 2 | Likely data entry error | Cap at 150 m² for scoring |
| Price = 0 | 3 | Invalid | Mark as error |
| No description | 1 | Situation detection fails | Manual review |

### DuckDB Queries

```sql
-- Top 10 largest properties
SELECT titulo, precio, m2, precio/m2 as €_per_m2
FROM viviendas_activas
WHERE m2 IS NOT NULL
ORDER BY m2 DESC LIMIT 10;

-- Price distribution by zone
SELECT ubicacion, COUNT(*) as count, 
       AVG(precio) as avg_price, AVG(precio/m2) as avg_€_per_m2
FROM viviendas_activas
WHERE precio IS NOT NULL AND m2 IS NOT NULL
GROUP BY ubicacion
ORDER BY avg_€_per_m2 DESC;

-- Data quality check
SELECT COUNT(*) as total,
       COUNT(CASE WHEN precio IS NULL THEN 1 END) as missing_price,
       COUNT(CASE WHEN m2 IS NULL THEN 1 END) as missing_m2
FROM viviendas_activas;
```

---

## Stage 3: LLM Scoring

**File:** `src/scoring.py`  
**LLM:** Ollama + Mistral 7B (local)

### Scoring Architecture

```
Per-property scoring:

Property Dict (15 fields)
    ↓
Prompt Template (Buy Box + property fields)
    ↓
Ollama API (local, http://localhost:11434)
    ↓
Raw Response (JSON + text)
    ↓
JSON Extraction (regex, cleanup)
    ↓
Structured Result (16+ fields)
    ↓
Storage (DataFrame → CSV)
```

### Prompt Engineering

**Constraint-based JSON schema:**

```
EXPECTED JSON OUTPUT:
{
  "kill_criteria": bool,
  "kill_razon": str | null,
  "score_ubicacion": 0-100,
  "score_estado": 0-100,
  "score_distribucion": 0-100,
  "score_patrimonio": 0-100,
  "score_financiero": 0-100,
  "bonuses": -50 to +50,
  "penalties": -50 to +50,
  "score_total": 0-100,           # = sum of components, capped
  "recomendacion": enum,           # "oportunidad fuerte" | "vale visita" | "solo si precio excelente" | "descartar"
  "justificacion": str,            # 1-2 sentence explanation
  "missing_critical_info": [str]   # Array of missing fields
}
```

**JSON Extraction (Robust):**

```python
def clean_json(text: str) -> str:
    """Extract JSON from potentially malformed response."""
    start = text.find("{")
    end = text.rfind("}") + 1
    
    if start == -1 or end == 0:
        raise ValueError("No JSON found")
    
    json_str = text[start:end]
    # Handle Python bool literals → JSON
    json_str = json_str.replace("True", "true")\
                      .replace("False", "false")\
                      .replace("None", "null")
    
    return json_str
```

### Scoring Weights

```
Final Score = 
    (location_score × 0.25) +
    (condition_score × 0.25) +
    (distribution_score × 0.20) +
    (financial_score × 0.20) +
    (intangible_score × 0.10) +
    bonuses -
    penalties

Final Score = max(0, min(100, Final Score))
```

### Kill Criteria (Hard Stops)

If ANY of these trigger, `score_total = 0`, `recommendation = "descartar"`:

```python
KILL_CRITERIA = [
    "kill_criteria == True",
    "price > €5,000/m² (non-penthouse)",
    "price < €800/m² (distress indicator)",
    "structural_damage || flooding_risk",
    "illegal_construction || disputed_ownership",
    "located_in_problematic_zone",
    "contaminated_land",
    "age > 50y AND systems_untouched",
    "HOA_fees > €300/month",
    "bare_ownership (nuda propiedad)",
]
```

### Performance Optimization

**Batch Processing:**
```python
BATCH_SIZE = 5  # Checkpoint every 5 properties
# Allows resumption if script crashes mid-run
```

**Rate Limiting:**
```python
time.sleep(1)  # 1-sec delay between Ollama requests
# Prevents overwhelming CPU/GPU; allows system to cool
```

**Conditional Prompting:**
```python
# If price missing → skip financial scoring
# If description empty → flag missing_critical_info
# Allows graceful degradation on incomplete data
```

### Output Schema

```python
DataFrame with 30+ columns:
├── Metadata
│   ├── url, titulo, ubicacion
│   ├── precio, m2, habitaciones, baños
│   ├── plataforma, tipo, estado, año
│   └── ascensor, planta
│
├── Scoring Components
│   ├── score_ubicacion, score_estado, score_distribucion
│   ├── score_patrimonio, score_financiero
│   ├── bonuses, penalties
│   └── score_total (final)
│
├── Recommendation
│   ├── recomendacion (enum)
│   ├── justificacion (text)
│   └── kill_criteria (bool)
│
└── Quality Flags
    ├── missing_critical_info (array)
    ├── data_quality_notes (text)
    └── _raw_response (original LLM output)
```

---

## Stage 4: Reporting & Visualization

**File:** `notebooks/04_scoring.ipynb`  
**Libraries:** Pandas, Matplotlib

### Report Flow

```python
# 1. Load scoring results
ranking = read_csv('data/output/ranking_final_*.csv')  # 59 scored

# 2. Merge with detailed data
activos = read_csv('data/processed/activos_*.csv')  # 136 total
entrega = ranking.merge(activos, on='url')  # 59 after merge

# 3. Filter recommendations
entrega = entrega[
    (entrega.recomendacion != 'descartar') &
    (entrega.score_total > 0)
]  # 40 final recommendations

# 4. Feature engineering
entrega['precio_m2'] = (entrega['precio'] / entrega['m2']).round(0)

# 5. Sorting
entrega = entrega.sort_values('score_total', ascending=False)

# 6. Visualization
scatter_plot('score_total' vs 'precio', colored by 'recomendacion')
bar_chart('precio_m2' by 'ubicacion')

# 7. Export
entrega.to_csv('data/output/report_casitas_[timestamp].pdf')
```

### Chart 1: Score vs Price

```
Scatter plot:
- X-axis: Listing price (€)
- Y-axis: Score (0-100)
- Color: Recommendation (oportunidad=green, visita=blue, etc.)
- Size: Area (m²)
- Annotations: Rank number (1, 2, 3...)

Purpose: Visual triage of portfolio
- Upper-left (good score, low price) = Best buys
- Lower-right (poor score, high price) = Overpriced
```

### Chart 2: Price/m² by Zone

```
Bar chart:
- X-axis: €/m² (3000-4500 typical)
- Y-axis: Zone names (Centro, El Palo, etc.)
- Colors: By median price tier
- Annotations: Zone count & mean

Purpose: Market comparison & zone selection
- Identify best value zones
- Spot outliers (unusually expensive/cheap areas)
```

### Deliverable Format (report_casitas_*.pdf)

**Columns (ranked by importance for investor):**

1. `rank` — Sort order (1 = best)
2. `score_total` — 0-100 composite score
3. `recomendacion` — Action label
4. `titulo` — Property name
5. `ubicacion` — Zone
6. `precio` — Listing price (€)
7. `m2` — Built area (m²)
8. `precio_m2` — Unit price (€/m²)
9. `habitaciones` — Bedrooms
10. `baños` — Bathrooms
11. `planta` — Floor
12. `ascensor` — Elevator access
13. `estado` — Condition (new/renovated/fair/needs work)
14. `año` — Construction year
15. `tipo` — Property type (apartment/townhouse/house)
16. `plataforma` — Source (Idealista/Fotocasa/etc.)
17. `url` — Direct link to listing
18. `justificacion` — Brief LLM reasoning
19. `kill_razon` — Why discarded (if applicable)
20. `missing_critical_info` — Data gaps flagged

---

## Data Flow Diagram (Detailed)

```
SOURCES (7 platforms)
    ↓
[01_scraper.ipynb]
    ├─ Idealista 44 URLs      ✓ 36 active, 8 down
    ├─ Fotocasa  7 URLs       ✓ 7 active
    ├─ Pisos.com 4 URLs       ✓ 2 active, 2 rental
    ├─ YaEncontre 12 URLs     ✓ 12 active
    ├─ Tecnocasa 2 URLs       ✓ 2 active
    └─ Habitaclia 4 URLs      ? Not started
    
    Output: data/raw/*_scraped_*.csv (297 records, 11 files)
    
    ↓
[02_analisis.ipynb]
    ├─ Deduplicate            (297 → 188)
    ├─ Filter active          (188 → 136)
    ├─ Detect situation       (125 libre, 11 other)
    └─ Type conversion        (str → int/float/date)
    
    Output: 
    - data/interim/todas_viviendas_*.csv (188)
    - data/processed/activos_*.csv (136)
    
    ↓
[src/scoring.py]
    ├─ Load Buy Box config    (25KB, ~50 rules)
    ├─ For each of 136 properties:
    │   ├─ Build prompt       (property fields + criteria)
    │   ├─ Query Ollama       (local LLM inference)
    │   ├─ Parse JSON         (extract 16 fields)
    │   └─ Validate score     (0-100, normalize recommendations)
    ├─ Error handling         (JSON parse errors → flag & continue)
    └─ Output to CSV
    
    Output: data/output/ranking_final_*.csv (59 scored)
    
    ↓
[04_scoring.ipynb]
    ├─ Load ranking           (59 scored)
    ├─ Merge with activos     (59 final)
    ├─ Filter recommendations (40 viable)
    ├─ Calculate metrics      (precio_m2, etc.)
    ├─ Generate charts
    └─ Export deliverable
    
    Output:
    - data/output/report_casitas_*.pdf (40 properties)
    - data/output/score_vs_precio.png
    - data/output/precio_m2_zona.png
```

---

## Error Handling & Resilience

### Scraping Errors

| Error | Cause | Recovery |
|-------|-------|----------|
| Connection timeout | Network issue | Retry with exponential backoff |
| Page structure changed | Platform update | Fall back to alternative selectors |
| Rate-limited (429) | Too many requests | Pause 5-10 min, resume |
| Cloudflare blocked | Bot detection | Use undetected-chromedriver |

### Data Quality Issues

| Issue | Severity | Handling |
|-------|----------|----------|
| Missing price | High | Skip from yield calc, warn in output |
| m² = 0 | Critical | Exclude from scoring |
| Price > €10M | Unlikely | Assume data entry error, cap/flag |
| Year > 2026 | Logic error | Set to NULL, handle gracefully |

### LLM Scoring Errors

| Error | Cause | Recovery |
|-------|-------|----------|
| JSON parse fail | Mistral format issue | Log error, mark property as error, continue |
| Timeout (>30s) | Model hung | Retry once, then skip |
| Ollama offline | Daemon crashed | Detect early, exit with clear message |

---

## Technology Stack

| Layer | Technology | Version | Purpose |
|-------|-----------|---------|---------|
| **Scraping** | Selenium/Undetected-ChromeDriver | Latest | Browser automation, anti-detection |
| **Parsing** | BeautifulSoup4 | 4.11+ | HTML parsing & CSS selectors |
| **Data Processing** | Pandas | 1.5+ | ETL, transformation, analysis |
| **Database** | DuckDB | 0.8+ | In-process SQL, fast queries |
| **LLM** | Ollama + Mistral 7B | Latest | Local inference, no API costs |
| **Visualization** | Matplotlib | 3.7+ | Charts & reporting |
| **Runtime** | Python | 3.9+ | Main scripting language |
| **Notebooks** | Jupyter | 7.0+ | Interactive development & reporting |

---

## Performance Characteristics

### Throughput

| Stage | Records/min | Time for 136 | Hardware |
|-------|------------|--------------|----------|
| Scrape | 2-4 | 30-70 min | Browser-based |
| Clean | 1000+ | 1-2 min | Local compute |
| Score | 4-8 | 17-34 min | Ollama (CPU) |
| Report | 500+ | 1-2 min | Local compute |

### Scalability

- **Current:** 136 properties; 40 recommended
- **Scalable to:** 1000+ properties (architecture supports)
- **Bottleneck:** LLM scoring (sequential, ~8s per property on CPU)
- **Improvement:** GPU acceleration (3-5x faster) or parallel Ollama instances

---

## Future Architecture Improvements

1. **API Integration:** Replace scraper with official Idealista/Fotocasa APIs (higher reliability)
2. **Streaming:** Real-time Kafka/Redis for live data updates
3. **Caching:** Redis to cache Ollama responses (identical properties → reuse scores)
4. **Parallelization:** Queue-based (Celery) scoring for 10x throughput
5. **Dashboards:** Web UI (Streamlit/Dash) for interactive filtering & alerts
6. **Model Ensemble:** Multi-model voting (Mistral + Neural-Chat) for robustness

---

**Last Updated:** 2026-07-24  
**Diagram Tool:** Mermaid / ASCII  
**Maintained By:** Casitas Project Team
