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




## What I took from this practice

- Figure out what one row represents before judging duplicates.
- Never assume a column's datatype is correct.
- Missing values and outliers need context before treatment.
- A technically clean table can still produce wrong business numbers.


