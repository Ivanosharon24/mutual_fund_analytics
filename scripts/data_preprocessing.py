import pandas as pd
import os

# Base project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Raw and processed paths
RAW_PATH = os.path.join(BASE_DIR, "data", "raw")
PROCESSED_PATH = os.path.join(BASE_DIR, "data", "processed")

# Create processed directory if it doesn't exist
os.makedirs(PROCESSED_PATH, exist_ok=True)

print("\nDATA PREPROCESSING STARTED\n")

# =====================================================
# CLEAN NAV HISTORY DATASET
# =====================================================

print("=" * 60)
print("Cleaning: 02_nav_history.csv")
print("=" * 60)

# Load dataset
nav_path = os.path.join(RAW_PATH, "02_nav_history.csv")

nav_df = pd.read_csv(nav_path)

# Initial shape
print("\nInitial Shape:")
print(nav_df.shape)

# Convert date column to datetime
nav_df["date"] = pd.to_datetime(nav_df["date"], errors="coerce")

# Remove invalid dates
nav_df = nav_df.dropna(subset=["date"])

# Sort by AMFI code and date
nav_df = nav_df.sort_values(by=["amfi_code", "date"])

# Remove duplicate rows
nav_df = nav_df.drop_duplicates()

# Validate NAV > 0
nav_df = nav_df[nav_df["nav"] > 0]

# Forward fill missing NAV values
nav_df["nav"] = nav_df.groupby("amfi_code")["nav"].ffill()

# Final shape
print("\nFinal Shape:")
print(nav_df.shape)

# Missing values
print("\nMissing Values:")
print(nav_df.isnull().sum())

# Save cleaned dataset
output_path = os.path.join(PROCESSED_PATH, "cleaned_nav_history.csv")

nav_df.to_csv(output_path, index=False)

print("\nCleaned NAV history saved successfully.")
# =====================================================
# CLEAN INVESTOR TRANSACTIONS DATASET
# =====================================================

print("\n" + "=" * 60)
print("Cleaning: 08_investor_transactions.csv")
print("=" * 60)

# Load dataset
transactions_path = os.path.join(RAW_PATH, "08_investor_transactions.csv")

transactions_df = pd.read_csv(transactions_path)

print("\nCOLUMN NAMES:")
print(transactions_df.columns)

# Initial shape
print("\nInitial Shape:")
print(transactions_df.shape)

# Standardize column names
transactions_df.columns = transactions_df.columns.str.lower().str.strip()

# Convert transaction_date to datetime
transactions_df["transaction_date"] = pd.to_datetime(
    transactions_df["transaction_date"],
    errors="coerce"
)

# Remove invalid dates
transactions_df = transactions_df.dropna(subset=["transaction_date"])

# Standardize transaction_type values
transactions_df["transaction_type"] = (
    transactions_df["transaction_type"]
    .str.strip()
    .str.title()
)

# Keep only valid transaction types
valid_transaction_types = ["Sip", "Lumpsum", "Redemption"]

transactions_df = transactions_df[
    transactions_df["transaction_type"].isin(valid_transaction_types)
]

# Validate amount > 0
#transactions_df = transactions_df[
   # transactions_df["amount"] > 0
#]

# Standardize KYC status
transactions_df["kyc_status"] = (
    transactions_df["kyc_status"]
    .str.strip()
    .str.upper()
)

# Allowed KYC values
valid_kyc = ["VERIFIED", "PENDING", "REJECTED"]

transactions_df = transactions_df[
    transactions_df["kyc_status"].isin(valid_kyc)
]

# Remove duplicates
transactions_df = transactions_df.drop_duplicates()

# Final shape
print("\nFinal Shape:")
print(transactions_df.shape)

# Missing values
print("\nMissing Values:")
print(transactions_df.isnull().sum())

# Unique transaction types
print("\nTransaction Types:")
print(transactions_df["transaction_type"].unique())

# Unique KYC statuses
print("\nKYC Statuses:")
print(transactions_df["kyc_status"].unique())

# Save cleaned dataset
output_path = os.path.join(
    PROCESSED_PATH,
    "cleaned_investor_transactions.csv"
)

transactions_df.to_csv(output_path, index=False)

print("\nCleaned investor transactions saved successfully.")
# =====================================================
# CLEAN SCHEME PERFORMANCE DATASET
# =====================================================

print("\n" + "=" * 60)
print("Cleaning: 07_scheme_performance.csv")
print("=" * 60)

# Load dataset
performance_path = os.path.join(
    RAW_PATH,
    "07_scheme_performance.csv"
)

performance_df = pd.read_csv(performance_path)

# Initial shape
print("\nInitial Shape:")
print(performance_df.shape)

# Standardize column names
performance_df.columns = (
    performance_df.columns
    .str.lower()
    .str.strip()
)

# Display columns
print("\nCOLUMN NAMES:")
print(performance_df.columns)

# Convert return columns to numeric
return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_columns:
    performance_df[col] = pd.to_numeric(
        performance_df[col],
        errors="coerce"
    )

# Remove rows with invalid return values
performance_df = performance_df.dropna(
    subset=return_columns
)

# Validate expense ratio range
performance_df = performance_df[
    (performance_df["expense_ratio_pct"] >= 0.1) &
(performance_df["expense_ratio_pct"] <= 2.5)
]

# Remove duplicates
performance_df = performance_df.drop_duplicates()

# Final shape
print("\nFinal Shape:")
print(performance_df.shape)

# Missing values
print("\nMissing Values:")
print(performance_df.isnull().sum())

# Summary statistics
print("\nRETURN SUMMARY:")
print(performance_df[return_columns].describe())

# Expense ratio summary
print("\nEXPENSE RATIO SUMMARY:")
print(performance_df["expense_ratio_pct"].describe())
# Save cleaned dataset
output_path = os.path.join(
    PROCESSED_PATH,
    "cleaned_scheme_performance.csv"
)

performance_df.to_csv(output_path, index=False)

print("\nCleaned scheme performance saved successfully.")