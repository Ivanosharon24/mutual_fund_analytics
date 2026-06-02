import pandas as pd
import os

# Path to raw data folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "raw")
# Get all CSV files
csv_files = [file for file in os.listdir(DATA_PATH) if file.endswith(".csv")]

print(f"\nFound {len(csv_files)} CSV files.\n")

for file in csv_files:

    file_path = os.path.join(DATA_PATH, file)

    print("=" * 80)
    print(f"FILE: {file}")
    print("=" * 80)

    try:
        df = pd.read_csv(file_path)

        print("\nSHAPE:")
        print(df.shape)

        print("\nDATA TYPES:")
        print(df.dtypes)

        print("\nFIRST 5 ROWS:")
        print(df.head())

        print("\nMISSING VALUES:")
        print(df.isnull().sum())

        print("\nDUPLICATE ROWS:")
        print(df.duplicated().sum())

    except Exception as e:
        print(f"\nERROR READING {file}")
        print(e)

    print("\n\n")