"""
Quick Start Guide - Using the Cleaned Dataset
==============================================

This script demonstrates how to load and begin analyzing the cleaned dataset.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Set display options for better readability
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 50)

print("="*100)
print("QUICK START GUIDE - RETAIL TRANSACTIONS ANALYSIS")
print("="*100)

# Load the cleaned dataset
print("\nLoading cleaned dataset...")
df = pd.read_csv('Retail_Transactions_Dataset_CLEANED.csv', parse_dates=['Date'])
print(f"✓ Loaded {df.shape[0]:,} rows and {df.shape[1]} columns")

# Display basic information
print("\n" + "="*100)
print("DATASET OVERVIEW")
print("="*100)
print(f"\nShape: {df.shape}")
print(f"Memory Usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
print(f"\nDate Range: {df['Date'].min()} to {df['Date'].max()}")
print(f"Number of Transactions: {df['Transaction_ID'].nunique():,}")
print(f"Number of Customers: {df['Customer_Name'].nunique():,}")
print(f"Number of Cities: {df['City'].nunique()}")

# Show column list
print("\n" + "="*100)
print("AVAILABLE COLUMNS")
print("="*100)
for i, col in enumerate(df.columns, 1):
    print(f"{i:2d}. {col:25s} ({str(df[col].dtype):15s})")

# Quick statistics
print("\n" + "="*100)
print("QUICK STATISTICS")
print("="*100)

print("\n📊 TRANSACTION METRICS:")
print(f"  • Total Revenue: ${df['Total_Cost'].sum():,.2f}")
print(f"  • Average Transaction Value: ${df['Total_Cost'].mean():.2f}")
print(f"  • Median Transaction Value: ${df['Total_Cost'].median():.2f}")
print(f"  • Average Items per Transaction: {df['Total_Items'].mean():.2f}")
print(f"  • Average Item Price: ${df['Avg_Item_Price'].mean():.2f}")

print("\n💳 PAYMENT METHODS:")
print(df['Payment_Method'].value_counts().to_string())

print("\n🏪 STORE TYPES:")
print(df['Store_Type'].value_counts().to_string())

print("\n🏙️ TOP 5 CITIES BY TRANSACTIONS:")
print(df['City'].value_counts().head().to_string())

print("\n👥 CUSTOMER CATEGORIES:")
print(df['Customer_Category'].value_counts().to_string())

print("\n🎁 PROMOTION USAGE:")
print(df['Promotion'].value_counts().to_string())

print("\n🛒 TRANSACTION SIZE DISTRIBUTION:")
print(df['Transaction_Size'].value_counts().to_string())

print("\n💰 PRICE CATEGORY DISTRIBUTION:")
print(df['Price_Category'].value_counts().to_string())

print("\n⏰ SHOPPING TIME DISTRIBUTION:")
print(df['Time_Period'].value_counts().to_string())

# Sample analysis examples
print("\n" + "="*100)
print("SAMPLE ANALYSIS EXAMPLES")
print("="*100)

# Example 1: Revenue by Year
print("\n1. Total Revenue by Year:")
revenue_by_year = df.groupby('Year')['Total_Cost'].sum()
for year, revenue in revenue_by_year.items():
    print(f"   {year}: ${revenue:,.2f}")

# Example 2: Average transaction by customer category
print("\n2. Average Transaction Value by Customer Category:")
avg_by_category = df.groupby('Customer_Category')['Total_Cost'].mean().sort_values(ascending=False)
for category, avg in avg_by_category.items():
    print(f"   {category:20s}: ${avg:.2f}")

# Example 3: Transactions by day of week
print("\n3. Busiest Days of the Week:")
transactions_by_day = df['DayOfWeek'].value_counts()
for day, count in transactions_by_day.items():
    print(f"   {day:10s}: {count:,} transactions")

# Example 4: Promotion effectiveness
print("\n4. Promotion Effectiveness:")
promo_stats = df.groupby('Promotion').agg({
    'Total_Cost': ['mean', 'sum', 'count']
}).round(2)
print(promo_stats)

# Example 5: Peak shopping hours
print("\n5. Top 5 Busiest Shopping Hours:")
busy_hours = df['Hour'].value_counts().head()
for hour, count in busy_hours.items():
    print(f"   {hour:02d}:00 - {count:,} transactions")

print("\n" + "="*100)
print("SAMPLE CODE SNIPPETS")
print("="*100)

print("""
# Load the dataset
df = pd.read_csv('Retail_Transactions_Dataset_CLEANED.csv', parse_dates=['Date'])

# Filter data
spring_2023 = df[(df['Year'] == 2023) & (df['Season'] == 'Spring')]
high_value = df[df['Price_Category'] == 'Premium']
morning_shoppers = df[df['Time_Period'] == 'Morning']

# Groupby analysis
revenue_by_city = df.groupby('City')['Total_Cost'].sum().sort_values(ascending=False)
avg_basket_by_store = df.groupby('Store_Type')['Total_Items'].mean()

# Time series analysis
monthly_revenue = df.groupby([df['Date'].dt.to_period('M')])['Total_Cost'].sum()

# Correlation analysis
numerical_cols = ['Total_Items', 'Total_Cost', 'Avg_Item_Price']
correlation_matrix = df[numerical_cols].corr()

# Customer analysis
customer_stats = df.groupby('Customer_Name').agg({
    'Transaction_ID': 'count',
    'Total_Cost': ['sum', 'mean'],
    'Total_Items': 'sum'
}).round(2)

# Promotion analysis
promo_vs_no_promo = df.groupby('Discount_Applied')['Total_Cost'].describe()

# Seasonal analysis
seasonal_revenue = df.groupby('Season')['Total_Cost'].agg(['sum', 'mean', 'count'])
""")

print("\n" + "="*100)
print("VISUALIZATION EXAMPLES")
print("="*100)

print("""
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)

# Revenue trend over time
df.groupby(df['Date'].dt.to_period('M'))['Total_Cost'].sum().plot(kind='line')
plt.title('Monthly Revenue Trend')
plt.xlabel('Month')
plt.ylabel('Total Revenue ($)')
plt.tight_layout()
plt.show()

# Distribution of transaction values
df['Total_Cost'].hist(bins=50, edgecolor='black')
plt.title('Distribution of Transaction Values')
plt.xlabel('Transaction Value ($)')
plt.ylabel('Frequency')
plt.show()

# Revenue by store type
df.groupby('Store_Type')['Total_Cost'].sum().plot(kind='bar')
plt.title('Total Revenue by Store Type')
plt.ylabel('Revenue ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Heatmap of transactions by day and hour
pivot = df.pivot_table(values='Transaction_ID', 
                       index='DayOfWeek', 
                       columns='Hour', 
                       aggfunc='count')
sns.heatmap(pivot, cmap='YlOrRd', fmt='d')
plt.title('Transaction Heatmap: Day vs Hour')
plt.tight_layout()
plt.show()
""")

print("\n" + "="*100)
print("✓ QUICK START GUIDE COMPLETE!")
print("="*100)
print("""
You're ready to start analyzing! The dataset is clean and feature-rich.

Next steps:
1. Run your own queries and filters
2. Create visualizations
3. Build predictive models
4. Generate business reports

For questions, refer to:
- data_dictionary.txt (variable definitions)
- transformation_log.txt (cleaning steps)
- PROJECT_SUMMARY.md (complete overview)
""")
