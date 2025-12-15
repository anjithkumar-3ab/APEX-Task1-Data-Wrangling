from pathlib import Path
import re
from typing import List

import pandas as pd

LIKELY_DATE_KEYS = [
    "date", "datetime", "orderdate", "order_date", "invoice_date",
    "transaction_date", "transdate", "purchase_date", "sale_date"
]


def _suspected_date_cols_from_names(columns: List[str]) -> List[str]:
    out = []
    for c in columns:
        lc = c.lower()
        if any(k in lc for k in LIKELY_DATE_KEYS):
            out.append(c)
    return out


def _detect_date_cols_by_sample(df: pd.DataFrame) -> List[str]:
    candidates = []
    for col in df.columns:
        sample = df[col].dropna().astype(str).head(25)
        if sample.empty:
            continue
        try:
            parsed = pd.to_datetime(sample, errors="coerce")
            if parsed.notna().mean() >= 0.6:
                candidates.append(col)
        except Exception:
            pass
    return candidates


def main():
    root = Path(__file__).resolve().parent.parent
    out_dir = root / "output"
    dd_csv = out_dir / "data_dictionary.csv"
    prof_md = out_dir / "profiling_summary.md"

    if not dd_csv.exists():
        raise FileNotFoundError("Expected output/data_dictionary.csv. Run data_wrangling.py first.")

    dd = pd.read_csv(dd_csv)

    # Identify issues
    high_missing = dd[dd["missing_pct"] >= 20.0][["column", "missing_pct"]].sort_values("missing_pct", ascending=False)

    num_cols = dd[dd["dtype"].str.contains("int|float|double|decimal|number", case=False, na=False)].copy()
    if "outliers_iqr" in num_cols.columns:
        num_cols["outlier_rate"] = (num_cols["outliers_iqr"].fillna(0) / num_cols["non_null"].replace(0, pd.NA)).astype(float)
        high_outliers = num_cols[num_cols["outlier_rate"] >= 0.05][["column", "outliers_iqr", "non_null", "outlier_rate"]].sort_values("outlier_rate", ascending=False)
    else:
        high_outliers = pd.DataFrame(columns=["column", "outliers_iqr", "non_null", "outlier_rate"])  # empty

    # Duplicate info from profiling summary
    dup_count = None
    if prof_md.exists():
        txt = prof_md.read_text(encoding="utf-8")
        m = re.search(r"Duplicate rows:\s*(\d+)", txt)
        if m:
            dup_count = int(m.group(1))

    # Heuristic detection of date columns on raw CSV
    raw_csv = root / "Retail_Transactions_Dataset.csv"
    suspected_dates = []
    if raw_csv.exists():
        try:
            raw_sample = pd.read_csv(raw_csv, nrows=1000)
            suspected_dates = sorted(set(_suspected_date_cols_from_names(raw_sample.columns) + _detect_date_cols_by_sample(raw_sample)))
        except Exception:
            pass

    # Feature engineering presence: check cleaned dataset
    cleaned_csv = out_dir / "retail_transactions_dataset_cleaned.csv"
    engineered = []
    if cleaned_csv.exists():
        try:
            cleaned = pd.read_csv(cleaned_csv, nrows=20)
            for col in ["TotalAmount", "Year", "Month", "DayOfWeek", "CustomerAge"]:
                if col in cleaned.columns:
                    engineered.append(col)
        except Exception:
            pass

    lines = ["# Data Quality Report\n"]

    # Top-level
    lines.append("## Overview")
    if dup_count is not None:
        lines.append(f"- Duplicate rows (in raw): {dup_count}")
    lines.append(f"- Columns: {len(dd)}")

    # Missingness
    lines.append("\n## High Missingness (>= 20%)")
    if high_missing.empty:
        lines.append("- None detected.")
    else:
        for _, r in high_missing.iterrows():
            lines.append(f"- {r['column']}: {r['missing_pct']}% missing")

    # Outliers
    lines.append("\n## Numeric Columns with High Outlier Rate (IQR, >= 5%)")
    if high_outliers.empty:
        lines.append("- None detected.")
    else:
        for _, r in high_outliers.iterrows():
            pct = round(float(r["outlier_rate"]) * 100, 2) if pd.notna(r["outlier_rate"]) else 0.0
            lines.append(f"- {r['column']}: {r['outliers_iqr']} of {r['non_null']} ({pct}%)")

    # Dates
    lines.append("\n## Suspected Date Columns")
    if suspected_dates:
        for c in suspected_dates:
            lines.append(f"- {c}")
    else:
        lines.append("- None detected via heuristics.")

    # Engineered features
    lines.append("\n## Engineered Features Present in Cleaned Dataset")
    if engineered:
        lines.append("- " + ", ".join(engineered))
    else:
        lines.append("- None (heuristics did not trigger).")

    # Suggestions
    lines.append("\n## Suggestions")
    lines.append("- Confirm true transaction date and price/quantity columns for stricter parsing and validations.")
    lines.append("- Define imputation policy per field (median/most-frequent) where applicable.")
    lines.append("- Standardize categorical values (e.g., country codes, product categories) with mapping tables.")

    out_path = out_dir / "quality_report.md"
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote quality report to: {out_path}")


if __name__ == "__main__":
    main()
