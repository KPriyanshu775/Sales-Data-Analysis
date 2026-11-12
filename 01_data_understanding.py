import pandas as pd
from pathlib import Path

# Step 1: Locate our dataset
file_path = Path("data/raw/sample_-_superstore (1).xls")

# Step 2: Check whether the file exists
if not file_path.exists():
    print("Dataset not found! Please check the file location.")
else:
    # Step 3: Load the Excel dataset
    df = pd.read_excel(file_path)

    # Step 4: Display the first five rows
    print("\n--- FIRST FIVE ROWS ---")
    print(df.head())

    # Step 5: Check the number of rows and columns
    print("\n--- DATASET SHAPE ---")
    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])

    # Step 6: Display column names
    print("\n--- COLUMN NAMES ---")
    print(df.columns.tolist())

    # Step 7: Check data types
    print("\n--- DATA TYPES ---")
    print(df.dtypes)

    # Step 8: Check missing values
    print("\n--- MISSING VALUES ---")
    print(df.isnull().sum())

    # Step 9: Check duplicate records
    print("\n--- DUPLICATE ROWS ---")
    print(df.duplicated().sum())

    # Step 10: Display numerical statistics
    print("\n--- NUMERICAL SUMMARY ---")
    print(df.describe())