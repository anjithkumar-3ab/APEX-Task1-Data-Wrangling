# Data Quality Report

## Overview
- Duplicate rows (in raw): 0
- Columns: 13

## High Missingness (>= 20%)
- Promotion: 33.39% missing

## Numeric Columns with High Outlier Rate (IQR, >= 5%)
- None detected.

## Suspected Date Columns
- Date

## Engineered Features Present in Cleaned Dataset
- Year, Month, DayOfWeek

## Suggestions
- Confirm true transaction date and price/quantity columns for stricter parsing and validations.
- Define imputation policy per field (median/most-frequent) where applicable.
- Standardize categorical values (e.g., country codes, product categories) with mapping tables.
