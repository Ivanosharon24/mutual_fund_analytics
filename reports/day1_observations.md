# Day 1 Data Ingestion Observations

## Summary

Successfully ingested and validated all 10 CSV datasets using Pandas.

## Key Findings

### 1. Dataset Integrity

* No duplicate rows detected across datasets.
* CSV structure and delimiters are consistent.
* No parser or encoding issues encountered.

### 2. Missing Values

* `04_monthly_sip_inflows.csv`

  * Column: `yoy_growth_pct`
  * Missing Values: 12
  * Likely due to unavailable previous-year comparison data.

### 3. Datatype Observations

* Several date columns are currently stored as strings:

  * `date`
  * `month`
  * `transaction_date`
  * `portfolio_date`
* These will require conversion using `pd.to_datetime()` during preprocessing.

### 4. Relational Structure

* `amfi_code` consistently appears across multiple datasets.
* Suitable for relational joins and schema modeling.

### 5. Initial Quality Assessment

* Data quality appears strong overall.
* No malformed records detected.
* Numeric fields largely mapped correctly to float/int types.

## Next Steps

* Data cleaning
* Datetime standardization
* AMFI code validation
* API-based NAV ingestion
* SQL schema preparation
