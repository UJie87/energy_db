# energy-db- Project README

This repo house our in-progress global-energy policy & datawarehouse. It is intentionally minimal yet scalable for the pilot phase.

## 1. Top-level layout

energy-db/
│
├── README.md              ← You are here
├── field_definitions.md   ← Unified data dictionary (all tables)
│
├── data/                  ← *raw* source files by country & topic
│   ├── taiwan/
│   │   └── ...
│   ├── vietnam/
│   │   ├── policy/
│   │   │   └── raw/
│   │   ├── capacity/
│   │   │   └── raw/
│   │   └── price_bracket/
│   │       └── raw/       ← 2024 price‑bracket XLS, PDFs…
│   └── processed/         ← theme‑level *clean* tables (multi‑country)
│       ├── price_bracket_clean.csv
│       └── capacity_clean.csv
│
├── scripts/               ← one script per country × topic
│   ├── fetch_taiwan_capacity.py
│   └── clean_price_bracket_vn.py
│
├── viz/                   ← notebooks / Power BI exports
└── output/summary_tables/ ← one‑off merged tables, slides, etc.

**Why this hybrid?**
| Need                           | Design choice                          |
|--------------------------------|----------------------------------------|
| Trace back to the orginal file | *raw* keep under `data/<country>/<topic>/raw` |
| Cross-country analysis in one step | clean table consolidated in `data/processed/` |
| Scripts remain simple | each script only worries one raw path |

## 2. Naming conventions
| Item | Rule/ Example |
|------|---------------|
| Country folders | lowercase English: `vietnam`, `taiwan` |
| Raw file name | `vn_price_bracket_2024_raw.csv` |
| Clean table | `<topic>_clean.csv` with country column inside |
| Policy ID | `VN_ELE_PRICE_2024` (ISO-2 + slug + year) |

## 3. Standard workflow (SOP)
1. Drop raw file into `data/<country>/<topic>/raw/.
2. Write/ Run a `clean_<topic>_<country>.py` script ->
   - read raw, tidy columns/ units
   - append or overwrite the master `data/processed/<topic>_clean.csv`
3. Add/ update fieldd definition in `field_definition.md` if new columns appear.
4. Commit & push (git add data scripts viz output && git commit -m "add vn 2024 price-bracket")
5. Create notebook/ dashboard under `viz/` as needed

> Re-running a clean scripts should be idempotent - it may replace that country-year slice inside the clean table but must not duplicate rows.

## 4. Price-Bracket example
- Raw XLS -> `data/vietnam/price_bracket/vn_price_bracket_2024_raw.xlsx`
- Script -> `scripts/clean_price_bracket_vn.py`
- Clean CSV -> `data/processed/price_bracket_clean.csv` (columns: `country, year, user_type, time_category, min_price, max_price, currency, source_policy_id`)
- Visuals -> `viz/price_bracket_beeswarm.ipynb`

## 5. Future evolution
- when volume grows, processed table can be loaded into DuckDB/ Prosgres without chaning file origins.
- consider moving long-term archives (PDFs, scans) to cloud storage with the same folder keys
- each team member owens **-> one country + topic scripts** to avoid merge chaos


