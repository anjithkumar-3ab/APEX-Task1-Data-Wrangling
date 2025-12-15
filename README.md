# Task 1 — Data Immersion & Wrangling

This project ingests the provided dataset, profiles data quality, builds a data dictionary, applies light cleaning/standardization, and exports an analysis‑ready CSV.

## What this includes
- Data dictionary (CSV + Markdown)
- Profiling summary (Markdown)
- Cleaned dataset (CSV)

## Quick start

### 1) Create a virtual environment and install deps (Windows PowerShell)
```powershell
Set-Location -Path "C:\Users\anjit\Desktop\APEX\TASK 1"
python -m venv .venv
& ".venv\Scripts\python.exe" -m pip install -U pip
& ".venv\Scripts\python.exe" -m pip install -r requirements.txt
```

### 2) Run the pipeline (defaults to `Retail_Transactions_Dataset.csv` in repo root)
```powershell
& ".venv\Scripts\python.exe" scripts\data_wrangling.py \
  --input "Retail_Transactions_Dataset.csv" \
  --output-dir "output"
```

Outputs will be created under `output/`:
- `data_dictionary.csv`
- `data_dictionary.md`
- `profiling_summary.md`
- `retail_transactions_cleaned.csv`
 - `quality_report.md`

## Notes on cleaning and transformations
- Trims whitespace in string columns.
- Attempts to parse and standardize any date-like columns to ISO format.
- Drops fully-empty columns and duplicate rows.
- Feature engineering (when columns exist):
  - `TotalAmount` = `Quantity` × (`UnitPrice` or `Price`)
  - Age at transaction (`CustomerAge`) if `DateOfBirth` and a transaction date are found
  - Date parts (`Year`, `Month`, `DayOfWeek`) from the detected transaction date column

This pipeline is intentionally conservative (it avoids destructive imputation). If you want specific imputations or categorization rules, tell me what you prefer and I’ll add them.
