# Pandas EDA — 7 Levels of Practice

Seven beginner-to-intermediate notebooks from my Exploratory Data Analysis learning roadmap, using a **synthetic sales dataset** with intentional data-quality issues.

My aim is to understand what the data is saying, not just memorize Pandas functions. The notebooks are short and meant to be read in order.

## Notebooks

| Notebook | What I practice |
| --- | --- |
| [00 — Loading datasets](notebooks/00_loading_data.ipynb) | CSV, Excel, JSON, `usecols`, data import checks |
| [01 — Dataset structure](notebooks/01_dataset_structure.ipynb) | `head`, `sample`, `shape`, `info`, dataset grain |
| [02 — Column inspection](notebooks/02_column_inspection.ipynb) | `unique`, `nunique`, `value_counts`, cardinality |
| [03 — Data types](notebooks/03_data_types.ipynb) | Dates, `to_numeric`, percentages, categorical columns |
| [04 — Descriptive statistics](notebooks/04_descriptive_statistics.ipynb) | `describe`, mean/median, quantiles, IQR, plots |
| [05 — Missing values](notebooks/05_missing_values.ipynb) | Missing percentages, investigation, cautious imputation |
| [06 — Duplicate analysis](notebooks/06_duplicate_analysis.ipynb) | Exact duplicates, business keys, legitimate repeats |

**Why Level 0–6?** My roadmap starts at Level 0, so that is seven notebooks. Level 7 (standardization and currency cleaning) is the next stage.

## Run locally

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS / Linux: source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

Start Jupyter in this folder, then open the files under `notebooks/`. Each notebook also works when the working directory is `notebooks/`.

## About the data

- `data/sales_raw.csv` — main dataset (565 rows, 15 columns); **fictional** transactions, not real customer data.
- `data/sales_sample.xlsx` — first 65 rows of the same data (for Excel loading practice).
- `data/sales_sample.json` — first 30 rows of the same data (for JSON loading practice).
- `data/data_dictionary.md` — column notes and intentionally added issues.

The raw data purposely includes blank cells, inconsistent city names, percentages saved as strings, an invalid date, a few bad quantity entries, repeated order IDs, exact duplicate records, and conflicting line IDs. The point is to **investigate** those issues rather than automatically delete everything suspicious.

## What I took from this practice

- Figure out what one row represents before judging duplicates.
- Never assume a column's datatype is correct.
- Missing values and outliers need context before treatment.
- A technically clean table can still produce wrong business numbers.

These are learning notebooks; they are not a production ETL pipeline. I plan to continue with Level 7 cleaning/standardization next.
