# Data Dictionary

**Column**: Transaction_ID
- Type: int64
- Non-null: 1000000
- Missing: 0 (0.0%)
- Unique: 1000000
- Min/Max: 1000000000.0 / 1000999999.0
- Mean/Std: 1000499999.5 / 288675.27893234405
- Outliers (IQR): 0.0

**Column**: Date
- Type: object
- Non-null: 1000000
- Missing: 0 (0.0%)
- Unique: 996337
- Top values: 2020-02-11 14:47:13: 3; 2024-03-13 12:44:06: 3; 2023-11-12 08:46:48: 3; 2020-03-11 20:38:45: 3; 2021-09-02 08:23:16: 3

**Column**: Customer_Name
- Type: object
- Non-null: 1000000
- Missing: 0 (0.0%)
- Unique: 329738
- Top values: Michael Smith: 454; Michael Johnson: 341; James Smith: 337; David Smith: 309; Michael Williams: 304

**Column**: Product
- Type: object
- Non-null: 1000000
- Missing: 0 (0.0%)
- Unique: 571947
- Top values: ['Toothpaste']: 4893; ['Deodorant']: 2541; ['Honey']: 2540; ['Eggs']: 2515; ['Vinegar']: 2505

**Column**: Total_Items
- Type: int64
- Non-null: 1000000
- Missing: 0 (0.0%)
- Unique: 10
- Min/Max: 1.0 / 10.0
- Mean/Std: 5.495941 / 2.871654187209311
- Outliers (IQR): 0.0

**Column**: Total_Cost
- Type: float64
- Non-null: 1000000
- Missing: 0 (0.0%)
- Unique: 9501
- Min/Max: 5.0 / 100.0
- Mean/Std: 52.45522040000001 / 27.416989145333183
- Outliers (IQR): 0.0

**Column**: Payment_Method
- Type: object
- Non-null: 1000000
- Missing: 0 (0.0%)
- Unique: 4
- Top values: Cash: 250230; Debit Card: 250074; Credit Card: 249985; Mobile Payment: 249711

**Column**: City
- Type: object
- Non-null: 1000000
- Missing: 0 (0.0%)
- Unique: 10
- Top values: Boston: 100566; Dallas: 100559; Seattle: 100167; Chicago: 100059; Houston: 100050

**Column**: Store_Type
- Type: object
- Non-null: 1000000
- Missing: 0 (0.0%)
- Unique: 6
- Top values: Supermarket: 166936; Pharmacy: 166915; Convenience Store: 166749; Warehouse Club: 166685; Department Store: 166614

**Column**: Discount_Applied
- Type: bool
- Non-null: 1000000
- Missing: 0 (0.0%)
- Unique: 2

**Column**: Customer_Category
- Type: object
- Non-null: 1000000
- Missing: 0 (0.0%)
- Unique: 8
- Top values: Senior Citizen: 125485; Homemaker: 125418; Teenager: 125319; Retiree: 125072; Student: 124842

**Column**: Season
- Type: object
- Non-null: 1000000
- Missing: 0 (0.0%)
- Unique: 4
- Top values: Spring: 250368; Fall: 250248; Winter: 249763; Summer: 249621

**Column**: Promotion
- Type: object
- Non-null: 666057
- Missing: 333943 (33.39%)
- Unique: 2
- Top values: Discount on Selected Items: 333370; BOGO (Buy One Get One): 332687
