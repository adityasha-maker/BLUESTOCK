from pathlib import Path
import pandas as pd

# Define directory and find all CSV files
RAW_DIR = Path("data/raw")
csv_files = list(RAW_DIR.glob("*.csv"))
print(f"Found {len(csv_files)} CSV files\n")

# Loop through and inspect each file
for file in csv_files:
    print("\n" + "=" * 80)
    print(f"FILE: {file.name}")
    print("=" * 80)
    
    try:
        df = pd.read_csv(file)
        
        print("Shape:")
        print(df.shape)
        
        print("\nDtypes:")
        print(df.dtypes)
        
        print("\nHead:")
        print(df.head())
        
        print("\nMissing Values:")
        print(df.isnull().sum())
        
        print("\nDuplicate Rows:")
        print(df.duplicated().sum())
        
    except Exception as e:
        print(f"Error reading {file.name}: {e}")
