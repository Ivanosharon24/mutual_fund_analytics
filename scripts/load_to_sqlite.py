import pandas as pd
import sqlite3
import os

# Base project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Paths
RAW_PATH = os.path.join(BASE_DIR, "data", "raw")
PROCESSED_PATH = os.path.join(BASE_DIR, "data", "processed")

# SQLite database path
db_path = os.path.join(BASE_DIR, "bluestock_mf.db")

# Create SQLite connection
conn = sqlite3.connect(db_path)

print("\nSQLITE DATABASE CREATED SUCCESSFULLY\n")

# =====================================================
# LOAD DIM_FUND
# =====================================================

print("=" * 60)
print("Loading dim_fund")
print("=" * 60)

fund_master_path = os.path.join(
    RAW_PATH,
    "01_fund_master.csv"
)

fund_df = pd.read_csv(fund_master_path)

# Select required columns
dim_fund = fund_df[
    [
        "amfi_code",
        "scheme_name",
        "fund_house",
        "category",
        "sub_category",
        "plan",
        "risk_category"
    ]
]

# Remove duplicates
dim_fund = dim_fund.drop_duplicates()

# Load to SQLite
dim_fund.to_sql(
    "dim_fund",
    conn,
    if_exists="replace",
    index=False
)

print(f"Rows loaded: {len(dim_fund)}")

# =====================================================
# LOAD FACT_NAV
# =====================================================

print("\n" + "=" * 60)
print("Loading fact_nav")
print("=" * 60)

nav_path = os.path.join(
    PROCESSED_PATH,
    "cleaned_nav_history.csv"
)

nav_df = pd.read_csv(nav_path)

nav_df.to_sql(
    "fact_nav",
    conn,
    if_exists="replace",
    index=False
)

print(f"Rows loaded: {len(nav_df)}")

# =====================================================
# LOAD FACT_TRANSACTIONS
# =====================================================

print("\n" + "=" * 60)
print("Loading fact_transactions")
print("=" * 60)

transactions_path = os.path.join(
    PROCESSED_PATH,
    "cleaned_investor_transactions.csv"
)

transactions_df = pd.read_csv(transactions_path)

transactions_df.to_sql(
    "fact_transactions",
    conn,
    if_exists="replace",
    index=False
)

print(f"Rows loaded: {len(transactions_df)}")

# =====================================================
# LOAD FACT_PERFORMANCE
# =====================================================

print("\n" + "=" * 60)
print("Loading fact_performance")
print("=" * 60)

performance_path = os.path.join(
    PROCESSED_PATH,
    "cleaned_scheme_performance.csv"
)

performance_df = pd.read_csv(performance_path)

performance_df.to_sql(
    "fact_performance",
    conn,
    if_exists="replace",
    index=False
)

print(f"Rows loaded: {len(performance_df)}")

# =====================================================
# VERIFY TABLES
# =====================================================

print("\n" + "=" * 60)
print("VERIFYING DATABASE TABLES")
print("=" * 60)

tables = pd.read_sql(
    """
    SELECT name
    FROM sqlite_master
    WHERE type='table';
    """,
    conn
)

print(tables)

# Close connection
conn.close()

print("\nDATABASE LOADING COMPLETED SUCCESSFULLY.")