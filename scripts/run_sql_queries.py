import sqlite3
import pandas as pd
import os

# Base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Database path
db_path = os.path.join(BASE_DIR, "bluestock_mf.db")

# Connect to SQLite
conn = sqlite3.connect(db_path)

print("\nCONNECTED TO SQLITE DATABASE\n")

# =====================================================
# QUERY 1 — TOP 5 FUNDS BY AUM
# =====================================================

query = """
SELECT
    scheme_name,
    fund_house,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;
"""

result = pd.read_sql(query, conn)

print("=" * 60)
print("TOP 5 FUNDS BY AUM")
print("=" * 60)

print(result)

# =====================================================
# QUERY 2 — TRANSACTION TYPE DISTRIBUTION
# =====================================================

query2 = """
SELECT
    transaction_type,
    COUNT(*) AS transaction_count
FROM fact_transactions
GROUP BY transaction_type
ORDER BY transaction_count DESC;
"""

result2 = pd.read_sql(query2, conn)

print("\n" + "=" * 60)
print("TRANSACTION TYPE DISTRIBUTION")
print("=" * 60)

print(result2)

# Close connection
conn.close()

print("\nSQL QUERY EXECUTION COMPLETED.")