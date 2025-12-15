import argparse
from pathlib import Path
from typing import List, Optional, Tuple

import pandas as pd


LIKELY_DATE_KEYS = [
    "date", "datetime", "orderdate", "order_date", "invoice_date",
    "transaction_date", "transdate", "purchase_date", "sale_date"
]

LIKELY_TXN_DATE_KEYS = [
    "transaction_date", "invoice_date", "order_date", "orderdate", "date"
]

DOB_KEYS = ["date_of_birth", "dob", "birthdate", "birth_date"]

QUANTITY_KEYS = ["quantity", "qty", "units", "unit_sold", "count"]

UNIT_PRICE_KEYS = ["unitprice", "unit_price", "price", "unit_cost", "unitcost"]


def find_first_matching_column(columns: List[str], candidates: List[str]) -> Optional[str]:
    lc = [c.lower() for c in columns]
    for cand in candidates:
        if cand in lc:
            return columns[lc.index(cand)]
    return None


def detect_date_columns(df: pd.DataFrame) -> List[str]:
    date_cols = []
    for col in df.columns:
        lc = col.lower()
        if any(k in lc for k in LIKELY_DATE_KEYS):
            date_cols.append(col)
            continue
        # Heuristic: try parsing a small sample
        sample = df[col].dropna().astype(str).head(20)
        if not sample.empty:
            try:
                parsed = pd.to_datetime(sample, errors="raise")
                # If majority parsed successfully, consider it a date
                if parsed.notna().mean() >= 0.8:
                    date_cols.append(col)
            except Exception:
                pass
    return date_cols


def standardize_dates_inplace(df: pd.DataFrame, date_cols: List[str]) -> None:
    for col in date_cols:
        try:
            df[col] = pd.to_datetime(df[col], errors="coerce")
        except Exception:
            # leave as-is if parsing fails
            continue


def add_feature_engineering(df: pd.DataFrame) -> None:
    # TotalAmount if Quantity and a unit price-like column exist
    q_col = find_first_matching_column(df.columns.tolist(), QUANTITY_KEYS)
    p_col = find_first_matching_column(df.columns.tolist(), UNIT_PRICE_KEYS)
    if q_col and p_col:
        with pd.option_context('mode.use_inf_as_na', True):
            try:
                df["TotalAmount"] = pd.to_numeric(df[q_col], errors="coerce") * pd.to_numeric(df[p_col], errors="coerce")
            except Exception:
                pass

    # Transaction date parts + CustomerAge if DOB exists
    txn_date_col = find_first_matching_column(df.columns.tolist(), LIKELY_TXN_DATE_KEYS)
    if txn_date_col and pd.api.types.is_datetime64_any_dtype(df[txn_date_col]):
        dt = df[txn_date_col]
        df["Year"] = dt.dt.year
        df["Month"] = dt.dt.month
        df["DayOfWeek"] = dt.dt.dayofweek

        dob_col = find_first_matching_column(df.columns.tolist(), DOB_KEYS)
        if dob_col is not None:
            try:
                dob = pd.to_datetime(df[dob_col], errors="coerce", infer_datetime_format=True)
                # Age at transaction in years (floor)
                age_days = (dt - dob).dt.days
                df["CustomerAge"] = (age_days / 365.25).astype("float").apply(lambda x: int(x) if pd.notna(x) else pd.NA)
            except Exception:
                pass


def strip_string_columns_inplace(df: pd.DataFrame) -> None:
    obj_cols = df.select_dtypes(include=["object", "string"]).columns
    for col in obj_cols:
        try:
            df[col] = df[col].astype("string").str.strip()
        except Exception:
            continue


def drop_empty_columns_inplace(df: pd.DataFrame) -> None:
    empty_cols = [c for c in df.columns if df[c].isna().all()]
    if empty_cols:
        df.drop(columns=empty_cols, inplace=True)


def profiling_summary(df: pd.DataFrame) -> Tuple[pd.DataFrame, str]:
    rows, cols = df.shape
    info_lines = [
        f"Row count: {rows}",
        f"Column count: {cols}",
    ]

    # Duplicate rows
    dup_count = df.duplicated().sum()
    info_lines.append(f"Duplicate rows: {dup_count}")

    # Per-column summary
    summaries = []
    for col in df.columns:
        s = df[col]
        dtype = s.dtype
        non_null = s.notna().sum()
        missing = s.isna().sum()
        missing_pct = (missing / len(s) * 100) if len(s) else 0.0
        unique = s.nunique(dropna=True)

        entry = {
            "column": col,
            "dtype": str(dtype),
            "non_null": int(non_null),
            "missing": int(missing),
            "missing_pct": round(float(missing_pct), 2),
            "unique": int(unique),
        }

        if pd.api.types.is_numeric_dtype(s):
            desc = s.describe(percentiles=[0.25, 0.5, 0.75])
            entry.update({
                "min": float(desc.get("min", pd.NA)) if pd.notna(desc.get("min", pd.NA)) else None,
                "mean": float(desc.get("mean", pd.NA)) if pd.notna(desc.get("mean", pd.NA)) else None,
                "std": float(desc.get("std", pd.NA)) if pd.notna(desc.get("std", pd.NA)) else None,
                "q1": float(desc.get("25%", pd.NA)) if pd.notna(desc.get("25%", pd.NA)) else None,
                "median": float(desc.get("50%", pd.NA)) if pd.notna(desc.get("50%", pd.NA)) else None,
                "q3": float(desc.get("75%", pd.NA)) if pd.notna(desc.get("75%", pd.NA)) else None,
                "max": float(desc.get("max", pd.NA)) if pd.notna(desc.get("max", pd.NA)) else None,
            })
            # IQR outlier count
            q1 = desc.get("25%", pd.NA)
            q3 = desc.get("75%", pd.NA)
            if pd.notna(q1) and pd.notna(q3):
                iqr = q3 - q1
                lower = q1 - 1.5 * iqr
                upper = q3 + 1.5 * iqr
                outliers = s[(s < lower) | (s > upper)].count()
                entry["outliers_iqr"] = int(outliers)
        else:
            # top 5 frequent values
            vc = s.value_counts(dropna=True).head(5)
            entry["top_values"] = "; ".join([f"{str(k)}: {int(v)}" for k, v in vc.items()])

        summaries.append(entry)

    dd_df = pd.DataFrame(summaries)

    # Markdown summary lines
    info_md = ["# Profiling Summary\n"] + [f"- {line}" for line in info_lines]
    return dd_df, "\n".join(info_md) + "\n"


def save_data_dictionary(dd_df: pd.DataFrame, output_dir: Path) -> None:
    csv_path = output_dir / "data_dictionary.csv"
    md_path = output_dir / "data_dictionary.md"

    dd_df.to_csv(csv_path, index=False)

    # Also emit a readable Markdown document
    lines = ["# Data Dictionary\n"]
    for _, row in dd_df.iterrows():
        lines.append(f"**Column**: {row['column']}")
        lines.append(f"- Type: {row['dtype']}")
        lines.append(f"- Non-null: {row['non_null']}")
        lines.append(f"- Missing: {row['missing']} ({row['missing_pct']}%)")
        lines.append(f"- Unique: {row['unique']}")
        if 'min' in row and pd.notna(row.get('min')):
            lines.append(f"- Min/Max: {row.get('min')} / {row.get('max')}")
        if 'mean' in row and pd.notna(row.get('mean')):
            lines.append(f"- Mean/Std: {row.get('mean')} / {row.get('std')}")
        if 'outliers_iqr' in row and pd.notna(row.get('outliers_iqr')):
            lines.append(f"- Outliers (IQR): {row.get('outliers_iqr')}")
        if 'top_values' in row and pd.notna(row.get('top_values')):
            lines.append(f"- Top values: {row.get('top_values')}")
        lines.append("")

    md_path.write_text("\n".join(lines), encoding="utf-8")


def export_cleaned(df: pd.DataFrame, output_dir: Path, input_name: str) -> Path:
    out_path = output_dir / (Path(input_name).stem.lower().replace(" ", "_") + "_cleaned.csv")

    # Format datetimes to ISO on export
    df_to_save = df.copy()
    for col in df_to_save.columns:
        if pd.api.types.is_datetime64_any_dtype(df_to_save[col]):
            # decide date vs datetime by time component presence
            series = df_to_save[col]
            has_time = series.dt.time.apply(lambda t: t != pd.Timestamp.min.time()).any()
            fmt = "%Y-%m-%d %H:%M:%S" if has_time else "%Y-%m-%d"
            df_to_save[col] = series.dt.strftime(fmt)
    df_to_save.to_csv(out_path, index=False)
    return out_path


def main():
    parser = argparse.ArgumentParser(description="Data wrangling: profile, dictionary, clean, and export")
    parser.add_argument("--input", type=str, default="Retail_Transactions_Dataset.csv", help="Input CSV path")
    parser.add_argument("--output-dir", type=str, default="output", help="Directory for outputs")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        # try relative to repo root
        alt = Path(__file__).resolve().parent.parent / input_path.name
        if alt.exists():
            input_path = alt
        else:
            raise FileNotFoundError(f"Input file not found: {args.input}")

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load CSV
    df = pd.read_csv(input_path, low_memory=False)

    # Profile + data dictionary
    dd_df, info_md = profiling_summary(df)
    (output_dir / "profiling_summary.md").write_text(info_md, encoding="utf-8")
    save_data_dictionary(dd_df, output_dir)

    # Cleaning / transformations
    strip_string_columns_inplace(df)
    date_cols = detect_date_columns(df)
    standardize_dates_inplace(df, date_cols)
    drop_empty_columns_inplace(df)
    df.drop_duplicates(inplace=True)

    # Feature engineering (best-effort)
    add_feature_engineering(df)

    # Export cleaned CSV
    out_csv = export_cleaned(df, output_dir, input_name=input_path.name)
    print(f"Wrote cleaned dataset to: {out_csv}")
    print(f"Wrote data dictionary and profiling to: {output_dir}")


if __name__ == "__main__":
    main()
