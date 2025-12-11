"""
Data Exploration and Quality Assessment
Task 1: Data Immersion & Wrangling
"""

import pandas as pd
import numpy as np
from datetime import datetime

# Load the dataset
print("Loading dataset...")
df = pd.read_csv('Retail_Transactions_Dataset.csv')

print("\n" + "="*80)
print("STEP 1: DATA ACCESS & FAMILIARIZATION")
print("="*80)

# Basic dataset information
print(f"\nDataset Shape: {df.shape[0]:,} rows × {df.shape[1]} columns")
print(f"\nMemory Usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")

# Display first few rows
print("\n--- First 5 Rows ---")
print(df.head())

# Display column names and data types
print("\n--- Column Information ---")
print(df.info())

# Display basic statistics
print("\n--- Statistical Summary ---")
print(df.describe(include='all'))

print("\n" + "="*80)
print("STEP 2: DATA QUALITY ASSESSMENT")
print("="*80)

# 1. Missing Values
print("\n--- Missing Values ---")
missing = df.isnull().sum()
missing_pct = (df.isnull().sum() / len(df)) * 100
missing_df = pd.DataFrame({
    'Missing_Count': missing,
    'Missing_Percentage': missing_pct
})
missing_df = missing_df[missing_df['Missing_Count'] > 0].sort_values('Missing_Count', ascending=False)
if len(missing_df) > 0:
    print(missing_df)
else:
    print("No missing values found!")

# 2. Duplicate Records
print("\n--- Duplicate Records ---")
duplicates = df.duplicated().sum()
print(f"Total duplicate rows: {duplicates:,}")
if duplicates > 0:
    print(f"Percentage of duplicates: {(duplicates/len(df))*100:.2f}%")

# 3. Data Type Assessment
print("\n--- Data Types Summary ---")
for col in df.columns:
    print(f"{col}: {df[col].dtype}")
    if df[col].dtype == 'object':
        print(f"  - Unique values: {df[col].nunique()}")
        print(f"  - Sample values: {df[col].dropna().unique()[:5]}")

# 4. Check for outliers in numerical columns
print("\n--- Outliers Detection (IQR Method) ---")
numerical_cols = df.select_dtypes(include=[np.number]).columns
for col in numerical_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    if len(outliers) > 0:
        print(f"{col}: {len(outliers):,} outliers ({(len(outliers)/len(df))*100:.2f}%)")
        print(f"  Range: [{df[col].min():.2f}, {df[col].max():.2f}]")
        print(f"  Expected range: [{lower_bound:.2f}, {upper_bound:.2f}]")

# 5. Inconsistent formatting checks
print("\n--- Formatting Consistency Checks ---")
for col in df.select_dtypes(include=['object']).columns:
    # Check for leading/trailing spaces
    has_spaces = df[col].astype(str).str.strip() != df[col].astype(str)
    if has_spaces.any():
        print(f"{col}: Has leading/trailing spaces in {has_spaces.sum()} rows")
    
    # Check for mixed case
    if df[col].dtype == 'object':
        unique_values = df[col].dropna().unique()
        if len(unique_values) > 0 and len(unique_values) < 100:
            print(f"{col}: Sample unique values = {list(unique_values[:10])}")

# 6. Date columns check
print("\n--- Date Column Analysis ---")
date_like_cols = [col for col in df.columns if 'date' in col.lower() or 'time' in col.lower()]
for col in date_like_cols:
    print(f"\n{col}:")
    print(f"  Data type: {df[col].dtype}")
    print(f"  Sample values: {df[col].head().tolist()}")
    if df[col].dtype == 'object':
        print("  ⚠️ Should be converted to datetime type")

# 7. Value range validation for numerical columns
print("\n--- Value Range Validation ---")
for col in numerical_cols:
    print(f"\n{col}:")
    print(f"  Min: {df[col].min()}")
    print(f"  Max: {df[col].max()}")
    print(f"  Mean: {df[col].mean():.2f}")
    print(f"  Median: {df[col].median():.2f}")
    print(f"  Std Dev: {df[col].std():.2f}")
    
    # Check for negative values where they shouldn't exist
    if 'price' in col.lower() or 'quantity' in col.lower() or 'amount' in col.lower():
        negative_count = (df[col] < 0).sum()
        if negative_count > 0:
            print(f"  ⚠️ {negative_count} negative values found!")

# 8. Categorical variables analysis
print("\n--- Categorical Variables Analysis ---")
categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    print(f"\n{col}:")
    print(f"  Unique values: {df[col].nunique()}")
    print(f"  Value counts:")
    print(df[col].value_counts().head(10))

print("\n" + "="*80)
print("DATA QUALITY ASSESSMENT COMPLETE")
print("="*80)

# Save summary to file
with open('data_quality_report.txt', 'w') as f:
    f.write("DATA QUALITY ASSESSMENT REPORT\n")
    f.write("="*80 + "\n\n")
    f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write(f"Dataset: Retail_Transactions_Dataset.csv\n")
    f.write(f"Total Records: {df.shape[0]:,}\n")
    f.write(f"Total Columns: {df.shape[1]}\n\n")
    
    f.write("Missing Values:\n")
    if len(missing_df) > 0:
        f.write(missing_df.to_string())
    else:
        f.write("No missing values found\n")
    
    f.write(f"\n\nDuplicate Records: {duplicates:,}\n")

print("\n✓ Quality assessment report saved to 'data_quality_report.txt'")
