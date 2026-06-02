import requests
import pandas as pd
import os

# Mutual fund schemes with AMFI codes
schemes = {
    "HDFC Top 100 Direct": 125497,
    "SBI Bluechip": 119551,
    "ICICI Bluechip": 120503,
    "Nippon Large Cap": 118632,
    "Axis Bluechip": 119092,
    "Kotak Bluechip": 120841
}

# Store API output
output_data = []

# Loop through each scheme
for fund_name, amfi_code in schemes.items():

    # API URL
    url = f"https://api.mfapi.in/mf/{amfi_code}"

    print(f"\nFetching NAV for: {fund_name}")

    # API request
    response = requests.get(url)

    # Check successful response
    if response.status_code == 200:

        # Convert JSON response to Python dictionary
        data = response.json()

        # Extract metadata
        meta = data.get("meta", {})

        # Extract NAV history
        nav_data = data.get("data", [])

        # Latest NAV entry
        latest_nav = nav_data[0] if nav_data else {}

        # Append required fields
        output_data.append({
            "amfi_code": amfi_code,
            "fund_name": fund_name,
            "scheme_name": meta.get("scheme_name"),
            "fund_house": meta.get("fund_house"),
            "scheme_type": meta.get("scheme_type"),
            "scheme_category": meta.get("scheme_category"),
            "latest_nav_date": latest_nav.get("date"),
            "latest_nav": latest_nav.get("nav")
        })

    else:
        print(f"Failed to fetch data for {fund_name}")

# Convert to DataFrame
df = pd.DataFrame(output_data)

# Dynamic project root path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Output CSV path
output_path = os.path.join(BASE_DIR, "data", "raw", "live_nav_snapshot.csv")

# Save CSV
df.to_csv(output_path, index=False)

print("\nLive NAV snapshot saved successfully.\n")

# Print final dataframe
print(df)