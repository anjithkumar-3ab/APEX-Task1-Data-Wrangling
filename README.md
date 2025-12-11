# 📊 TASK 1: Data Immersion & Wrangling

## APEX Internship Program - Complete Deliverable Package

---

## 🎯 Project Overview

This project demonstrates comprehensive data wrangling skills on a **1,000,000-row retail transactions dataset**. All tasks have been completed successfully, resulting in a clean, analysis-ready dataset with enhanced features.

**Status:** ✅ **COMPLETED**  
**Date:** December 11, 2025  
**Dataset:** Retail Transactions (1M records)

---

## 📁 Project Structure

```text
TASK 1/
│
├── 📄 README.md                                    # This file - Project overview
├── 📄 PROJECT_SUMMARY.md                           # Comprehensive project report
│
├── 📊 DATA FILES
│   ├── Retail_Transactions_Dataset.csv             # Original dataset (1M rows)
│   ├── Retail_Transactions_Dataset_CLEANED.csv     # ✅ Final cleaned dataset (1M rows, 23 columns)
│   └── Retail_Transactions_Dataset_SAMPLE.csv      # Sample dataset (1,000 rows)
│
├── 🐍 PYTHON SCRIPTS
│   ├── 01_data_exploration.py                      # Data exploration & quality assessment
│   ├── 02_data_dictionary.py                       # Data dictionary generation
│   ├── 03_data_cleaning.py                         # ⭐ Main cleaning & transformation script
│   └── 04_quick_start_guide.py                     # Usage guide & examples
│
└── 📝 DOCUMENTATION
    ├── data_dictionary.txt                         # Complete variable documentation
    ├── data_quality_report.txt                     # Initial quality assessment
    └── transformation_log.txt                      # Detailed transformation log
```

---

## ✨ Key Achievements

### 1️⃣ Data Access & Familiarization ✅

- ✅ Loaded and analyzed 1,000,000 records
- ✅ Documented all 13 original variables
- ✅ Created comprehensive data dictionary
- ✅ Identified business relevance for each field

### 2️⃣ Data Quality Assessment ✅

- ✅ Detected 1 column with missing values (33.39%)
- ✅ Confirmed zero duplicate records
- ✅ Validated all categorical variables
- ✅ Identified date format issues
- ✅ Checked for outliers (none found)

### 3️⃣ Data Cleaning & Transformation ✅

- ✅ Converted date strings to datetime format
- ✅ Filled 333,943 missing values meaningfully
- ✅ Standardized all text fields
- ✅ Validated data types
- ✅ Created 10 new analytical features
- ✅ Produced final analysis-ready dataset

---

## 🚀 Quick Start

### Option 1: Use the Cleaned Dataset Directly

```python
import pandas as pd

# Load the cleaned dataset
df = pd.read_csv('Retail_Transactions_Dataset_CLEANED.csv', parse_dates=['Date'])

# Start analyzing!
print(df.head())
print(df.info())
```

### Option 2: Run the Complete Pipeline

```bash
# Step 1: Explore the data
python 01_data_exploration.py

# Step 2: Generate data dictionary
python 02_data_dictionary.py

# Step 3: Clean and transform (produces final dataset)
python 03_data_cleaning.py

# Step 4: See usage examples
python 04_quick_start_guide.py
```

---

## 📊 Dataset Details

### Original Dataset

- **Records:** 1,000,000 transactions
- **Variables:** 13 columns
- **Size:** ~631 MB
- **Date Range:** 2020-01-01 to 2024-05-18
- **Issues Found:** 2 (date format, missing values)

### Cleaned Dataset

- **Records:** 1,000,000 (maintained)
- **Variables:** 23 columns (enriched)
- **Missing Values:** 0
- **Duplicates:** 0
- **Quality Score:** 100% ✅
- **Status:** **ANALYSIS-READY**

### New Features Added (10 total)

1. **Year** - Extracted from date
2. **Month** - Extracted from date
3. **Day** - Extracted from date
4. **DayOfWeek** - Day name (Monday-Sunday)
5. **Hour** - Hour of day (0-23)
6. **Quarter** - Quarter (Q1-Q4)
7. **Time_Period** - Shopping period (Morning/Afternoon/Evening/Night)
8. **Avg_Item_Price** - Total_Cost / Total_Items
9. **Transaction_Size** - Basket size (Small/Medium/Large/Extra Large)
10. **Price_Category** - Value segment (Low/Medium/High/Premium)

---

## 📈 Key Statistics

| Metric | Value |
|--------|-------|
| Total Revenue | $52,455,220.40 |
| Avg Transaction Value | $52.46 |
| Avg Items per Transaction | 5.5 |
| Unique Customers | 329,738 |
| Cities Covered | 10 |
| Store Types | 6 |
| Payment Methods | 4 |
| Customer Segments | 8 |
| Transactions with Promotions | 66.61% |

---

## 📚 Documentation Files

### 1. [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)

Comprehensive project report including:

- Executive summary
- Detailed methodology
- Data quality improvements
- Business insights
- Technical notes

### 2. [data_dictionary.txt](data_dictionary.txt)

Complete documentation of all 23 variables:

- Data types and formats
- Business relevance
- Quality notes
- Transformation recommendations

### 3. [data_quality_report.txt](data_quality_report.txt)

Initial quality assessment:

- Missing value analysis
- Duplicate detection
- Outlier identification
- Consistency checks

### 4. [transformation_log.txt](transformation_log.txt)

Detailed transformation record:

- All cleaning operations
- Feature engineering steps
- Before/after comparisons
- Final quality metrics

---

## 💡 Sample Analysis Examples

### Revenue Analysis

```python
# Total revenue by year
df.groupby('Year')['Total_Cost'].sum()

# Revenue by store type
df.groupby('Store_Type')['Total_Cost'].sum().sort_values(ascending=False)

# Monthly revenue trend
df.groupby(df['Date'].dt.to_period('M'))['Total_Cost'].sum().plot()
```

### Customer Analysis

```python
# Average transaction by customer category
df.groupby('Customer_Category')['Total_Cost'].mean().sort_values(ascending=False)

# Customer frequency
df.groupby('Customer_Name')['Transaction_ID'].count().sort_values(ascending=False)
```

### Time Analysis

```python
# Busiest days of the week
df['DayOfWeek'].value_counts()

# Peak shopping hours
df['Hour'].value_counts().sort_index()

# Seasonal patterns
df.groupby('Season')['Total_Cost'].agg(['sum', 'mean', 'count'])
```

### Promotion Effectiveness

```python
# Compare promotion types
df.groupby('Promotion')['Total_Cost'].agg(['mean', 'sum', 'count'])

# Discount impact
df.groupby('Discount_Applied')['Total_Cost'].describe()
```

---

## 🛠️ Technical Details

### Tools & Libraries

- **Python 3.x**
- **Pandas** - Data manipulation
- **NumPy** - Numerical operations
- **DateTime** - Temporal handling

### Requirements

```python
pandas>=1.3.0
numpy>=1.21.0
```

### Performance

- **Processing Time:** ~5 minutes for 1M records
- **Memory Usage:** ~866 MB (loaded dataset)
- **Optimized:** Memory-efficient operations

---

## ✅ Quality Assurance

All data quality checks passed:

- ✅ No missing values in critical columns
- ✅ No duplicate transaction IDs
- ✅ No negative prices or quantities
- ✅ All dates properly formatted
- ✅ All categorical variables validated
- ✅ All features correctly calculated
- ✅ Output files generated successfully

---

## 🎓 Skills Demonstrated

1. **Data Engineering**
   - Large dataset handling
   - ETL pipeline development
   - Feature engineering

2. **Data Quality Management**
   - Missing value treatment
   - Outlier detection
   - Data validation

3. **Python Programming**
   - Pandas operations
   - DataFrame manipulation
   - Code optimization

4. **Documentation**
   - Comprehensive reporting
   - Data dictionaries
   - Technical writing

5. **Business Understanding**
   - Domain knowledge application
   - Feature relevance assessment
   - Insight generation

---

## 🚀 Next Steps

The cleaned dataset is ready for:

1. **Exploratory Data Analysis (EDA)**
   - Distribution analysis
   - Correlation studies
   - Pattern identification

2. **Business Intelligence**
   - Dashboard creation
   - KPI tracking
   - Performance reporting

3. **Advanced Analytics**
   - Customer segmentation
   - Market basket analysis
   - Demand forecasting

4. **Machine Learning**
   - Predictive modeling
   - Customer lifetime value
   - Recommendation systems

---

## 📞 Support

For questions or issues:

1. Review [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) for comprehensive details
2. Check [data_dictionary.txt](data_dictionary.txt) for variable definitions
3. Run [04_quick_start_guide.py](04_quick_start_guide.py) for usage examples
4. Examine [transformation_log.txt](transformation_log.txt) for transformation details

---

## 🏆 Project Status

### TASK 1 COMPLETED SUCCESSFULLY

All objectives achieved:

- ✅ Data accessed and familiarized
- ✅ Complete data dictionary created
- ✅ Comprehensive quality assessment performed
- ✅ Data cleaned and transformed
- ✅ Analysis-ready dataset produced
- ✅ Documentation comprehensive and clear

**Ready for:** Immediate use in analysis, reporting, and modeling projects.

---

## 📝 Changelog

### Version 1.0 - December 11, 2025

- ✅ Initial data exploration completed
- ✅ Data dictionary generated
- ✅ Data cleaning pipeline implemented
- ✅ Feature engineering completed
- ✅ Final dataset produced
- ✅ Documentation finalized

---

## 📄 License

This project is part of the APEX Internship Program.

---

*Last Updated: December 11, 2025*  
*Project: APEX Internship - Task 1: Data Immersion & Wrangling*
