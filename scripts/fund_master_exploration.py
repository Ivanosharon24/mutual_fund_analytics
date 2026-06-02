import pandas as pd
import os

# Base project path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# File path
file_path = os.path.join(BASE_DIR, "data", "raw", "01_fund_master.csv")

# Load dataset
df = pd.read_csv(file_path)

print("\nDATASET SHAPE:")
print(df.shape)

# Unique fund houses
print("\nUNIQUE FUND HOUSES:")
print(df["fund_house"].nunique())
print(df["fund_house"].unique())

# Categories
print("\nUNIQUE CATEGORIES:")
print(df["category"].unique())

# Sub-categories
print("\nUNIQUE SUB-CATEGORIES:")
print(df["sub_category"].unique())

# Risk categories
print("\nUNIQUE RISK CATEGORIES:")
print(df["risk_category"].unique())

# Plan types
print("\nPLAN TYPES:")
print(df["plan"].unique())