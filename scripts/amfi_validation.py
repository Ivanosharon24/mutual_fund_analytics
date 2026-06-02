import pandas as pd
import os

# Base project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# File paths
fund_master_path = os.path.join(BASE_DIR, "data", "raw", "01_fund_master.csv")
nav_history_path = os.path.join(BASE_DIR, "data", "raw", "02_nav_history.csv")

# Load datasets
fund_master = pd.read_csv(fund_master_path)
nav_history = pd.read_csv(nav_history_path)

# Extract unique AMFI codes
master_codes = set(fund_master["amfi_code"].unique())
nav_codes = set(nav_history["amfi_code"].unique())

# Validation
missing_codes = master_codes - nav_codes

# Results
print("\nAMFI VALIDATION SUMMARY")
print("=" * 50)

print(f"\nTotal AMFI codes in fund_master: {len(master_codes)}")
print(f"Total AMFI codes in nav_history: {len(nav_codes)}")
print(f"Missing codes in nav_history: {len(missing_codes)}")

# Show missing codes if any
if missing_codes:
    print("\nMissing AMFI Codes:")
    print(missing_codes)
else:
    print("\nAll AMFI codes validated successfully.")