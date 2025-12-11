"""
DATA DICTIONARY
Retail Transactions Dataset
Generated: December 11, 2025
"""

data_dictionary = {
    "Transaction_ID": {
        "data_type": "Integer (int64)",
        "description": "Unique identifier for each retail transaction",
        "range": "1,000,000,000 to 1,000,999,999",
        "business_relevance": "Primary key for tracking and referencing individual transactions. Essential for transaction-level analysis and avoiding duplication.",
        "quality_notes": "No missing values, no duplicates detected"
    },
    
    "Date": {
        "data_type": "String (Object) - Should be DateTime",
        "description": "Date and time when the transaction occurred",
        "format": "YYYY-MM-DD HH:MM:SS",
        "range": "2020-01-01 to 2024-12-31 (approximate)",
        "business_relevance": "Critical for time-series analysis, seasonal trends, peak shopping hours, and year-over-year comparisons. Enables temporal pattern analysis.",
        "quality_notes": "Currently stored as string - needs conversion to datetime type for proper analysis",
        "recommended_transformation": "Convert to datetime64[ns] type"
    },
    
    "Customer_Name": {
        "data_type": "String (Object)",
        "description": "Full name of the customer who made the transaction",
        "unique_values": "329,738 unique customers",
        "business_relevance": "Identifies repeat customers for loyalty analysis, customer lifetime value calculation, and personalized marketing. Note: Multiple customers may share the same name.",
        "quality_notes": "Most common name: 'Michael Smith' with 454 occurrences. Names appear properly formatted.",
        "privacy_consideration": "Contains PII (Personally Identifiable Information) - handle according to data privacy regulations"
    },
    
    "Product": {
        "data_type": "String (Object) - List representation",
        "description": "List of products purchased in the transaction, stored as string representation of Python list",
        "format": "['Product1', 'Product2', ...]",
        "unique_values": "571,947 unique product combinations",
        "business_relevance": "Essential for product affinity analysis, market basket analysis, inventory management, and understanding purchase patterns. Can identify frequently bought together items.",
        "quality_notes": "Stored as string representation of list - may need parsing for detailed product-level analysis",
        "recommended_transformation": "Parse string to actual list for product-level analysis; consider splitting into separate rows for item-level analysis"
    },
    
    "Total_Items": {
        "data_type": "Integer (int64)",
        "description": "Total number of items purchased in the transaction",
        "range": "1 to 10 items",
        "mean": "5.5 items",
        "median": "5 items",
        "business_relevance": "Indicates basket size, useful for understanding shopping patterns, average transaction volume, and for segmenting small vs. large purchases.",
        "quality_notes": "No missing values, uniform distribution, no outliers detected",
        "insights": "Reasonable range suggests controlled product selection per transaction"
    },
    
    "Total_Cost": {
        "data_type": "Float (float64)",
        "description": "Total monetary value of the transaction in dollars",
        "range": "$5.00 to $100.00",
        "mean": "$52.46",
        "median": "$52.42",
        "std_dev": "$27.42",
        "business_relevance": "Key revenue metric for calculating total sales, average transaction value, revenue trends, and identifying high-value transactions. Critical for financial reporting.",
        "quality_notes": "No missing values, no negative values detected, no outliers",
        "insights": "Relatively balanced distribution around $52, suggesting consistent pricing structure"
    },
    
    "Payment_Method": {
        "data_type": "String (Object) - Categorical",
        "description": "Method of payment used for the transaction",
        "categories": ["Cash", "Debit Card", "Credit Card", "Mobile Payment"],
        "distribution": "Fairly evenly distributed (~25% each)",
        "business_relevance": "Important for understanding customer payment preferences, processing fee calculation, and optimizing payment infrastructure. Can inform digital transformation initiatives.",
        "quality_notes": "No missing values, clean categorical data, well-formatted",
        "insights": "Balanced usage across all payment methods indicates diverse customer preferences"
    },
    
    "City": {
        "data_type": "String (Object) - Categorical",
        "description": "City where the transaction took place",
        "categories": ["Boston", "Dallas", "Seattle", "Chicago", "Houston", "New York", "Los Angeles", "Miami", "San Francisco", "Atlanta"],
        "total_cities": 10,
        "distribution": "Relatively balanced (~10% each city)",
        "business_relevance": "Enables geographic analysis, regional performance comparison, targeted marketing, and location-based inventory decisions. Critical for expansion planning.",
        "quality_notes": "No missing values, consistent formatting",
        "insights": "Multi-city presence with fairly uniform transaction distribution"
    },
    
    "Store_Type": {
        "data_type": "String (Object) - Categorical",
        "description": "Type of retail store where the transaction occurred",
        "categories": ["Supermarket", "Pharmacy", "Convenience Store", "Warehouse Club", "Department Store", "Specialty Store"],
        "total_types": 6,
        "distribution": "Evenly distributed (~16-17% each)",
        "business_relevance": "Critical for channel analysis, understanding shopping preferences by store format, optimizing product assortment by store type, and competitive positioning.",
        "quality_notes": "No missing values, consistent formatting",
        "insights": "Diverse retail channel representation"
    },
    
    "Discount_Applied": {
        "data_type": "Boolean (bool)",
        "description": "Indicates whether any discount was applied to the transaction",
        "values": "True/False",
        "business_relevance": "Essential for measuring promotion effectiveness, understanding price sensitivity, calculating discount impact on revenue, and optimizing promotional strategies.",
        "quality_notes": "No missing values, proper boolean type",
        "analysis_opportunity": "Correlate with Total_Cost and Promotion columns to measure discount impact"
    },
    
    "Customer_Category": {
        "data_type": "String (Object) - Categorical",
        "description": "Demographic or lifestyle segment of the customer",
        "categories": ["Senior Citizen", "Homemaker", "Teenager", "Retiree", "Student", "Professional", "Middle-Aged", "Young Adult"],
        "total_categories": 8,
        "distribution": "Relatively balanced (~12-13% each)",
        "business_relevance": "Crucial for customer segmentation, targeted marketing, product recommendation, understanding demographic preferences, and tailoring customer experience.",
        "quality_notes": "No missing values, consistent categories",
        "insights": "Diverse customer base across all life stages"
    },
    
    "Season": {
        "data_type": "String (Object) - Categorical",
        "description": "Season during which the transaction occurred",
        "categories": ["Spring", "Fall", "Winter", "Summer"],
        "total_seasons": 4,
        "distribution": "Fairly balanced (~25% each)",
        "business_relevance": "Enables seasonal trend analysis, demand forecasting, seasonal inventory planning, and understanding seasonality impact on sales patterns.",
        "quality_notes": "No missing values, consistent formatting",
        "derived_from": "Likely derived from Date column",
        "insights": "Balanced seasonal coverage for comprehensive year-round analysis"
    },
    
    "Promotion": {
        "data_type": "String (Object) - Categorical",
        "description": "Type of promotional campaign active during the transaction (if any)",
        "categories": ["BOGO (Buy One Get One)", "Discount on Selected Items", None],
        "total_types": "2 (plus NULL)",
        "missing_percentage": "33.39%",
        "distribution": "When present, evenly split between the two promotion types",
        "business_relevance": "Critical for promotion effectiveness analysis, ROI calculation, understanding which promotions drive sales, and planning future campaigns.",
        "quality_notes": "33.39% missing values - represents transactions without active promotions",
        "interpretation": "NULL values are meaningful - indicate no promotion was active",
        "recommended_treatment": "Fill NULL values with 'No Promotion' for clarity in analysis"
    }
}

# Print formatted data dictionary
print("="*100)
print("COMPREHENSIVE DATA DICTIONARY - RETAIL TRANSACTIONS DATASET")
print("="*100)
print(f"\nDataset Overview:")
print(f"  • Total Records: 1,000,000 transactions")
print(f"  • Total Variables: 13 columns")
print(f"  • Date Range: ~2020 to 2024")
print(f"  • File Size: ~631 MB")
print(f"  • Data Quality: High (minimal issues)")

print("\n" + "="*100)
print("VARIABLE DEFINITIONS")
print("="*100)

for i, (var_name, details) in enumerate(data_dictionary.items(), 1):
    print(f"\n{i}. {var_name}")
    print("-" * 100)
    for key, value in details.items():
        key_formatted = key.replace("_", " ").title()
        print(f"   {key_formatted}: {value}")

# Summary statistics
print("\n" + "="*100)
print("DATA QUALITY SUMMARY")
print("="*100)
print("""
Key Findings:
✓ STRENGTHS:
  • No duplicate records
  • Only 1 variable with missing values (Promotion: 33.39% - intentional/meaningful)
  • Consistent formatting across categorical variables
  • No data type mismatches for numerical/boolean variables
  • No outliers detected in numerical variables
  • Balanced distributions across most categorical variables
  • High data integrity overall

⚠ AREAS FOR IMPROVEMENT:
  • Date column stored as string - needs conversion to datetime
  • Product column stored as string representation of list - may need parsing
  • Promotion column has NULL values - should be labeled as 'No Promotion' for clarity
  • Customer names may have duplicates (common names) - consider adding Customer_ID

📊 BUSINESS INSIGHTS:
  • Diverse customer base across 8 demographic segments
  • Multi-channel presence across 6 store types
  • Geographic coverage across 10 major US cities
  • Modern payment mix with 25% mobile payments
  • Average transaction: $52.46 with 5.5 items
  • Balanced seasonal coverage for trend analysis
  • 66.61% of transactions have active promotions
""")

# Save to file
with open('data_dictionary.txt', 'w', encoding='utf-8') as f:
    f.write("="*100 + "\n")
    f.write("COMPREHENSIVE DATA DICTIONARY - RETAIL TRANSACTIONS DATASET\n")
    f.write("="*100 + "\n\n")
    
    for var_name, details in data_dictionary.items():
        f.write(f"\n{var_name}\n")
        f.write("-" * 100 + "\n")
        for key, value in details.items():
            key_formatted = key.replace("_", " ").title()
            f.write(f"{key_formatted}: {value}\n")

print("\n✓ Data dictionary saved to 'data_dictionary.txt'")
