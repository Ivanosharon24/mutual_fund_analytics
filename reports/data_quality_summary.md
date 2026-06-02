# Data Quality Summary

## Overview

A comprehensive data ingestion and validation process was completed across 10 mutual fund datasets along with live NAV API integration.

---

## Dataset Validation Results

### 1. Duplicate Record Check

* No duplicate rows detected across datasets.
* Dataset uniqueness appears consistent.

### 2. Missing Value Analysis

* `04_monthly_sip_inflows.csv`

  * Column: `yoy_growth_pct`
  * Missing Values: 12
  * Reason: Historical YoY comparison unavailable for initial periods.

### 3. Datatype Assessment

Several date-related columns are currently stored as string/object datatypes:

* `date`
* `month`
* `transaction_date`
* `portfolio_date`

These require conversion using:

```python
pd.to_datetime()
```

### 4. Referential Integrity Validation

* `amfi_code` was validated between:

  * `01_fund_master.csv`
  * `02_nav_history.csv`
* Validation confirms relational consistency.

### 5. API Integration Validation

Successfully fetched live NAV data from:

* `https://api.mfapi.in`

Generated:

* `live_nav_snapshot.csv`

### 6. Data Structure Quality

* CSV formatting is consistent.
* No parser errors encountered.
* Numeric fields mapped correctly to int/float types.

---

## Business Understanding Gained

### Risk Categories Identified

* Low
* Moderate
* Moderately High
* High
* Very High

### Plan Types Identified

* Regular
* Direct

---

## Next Phase

* Data preprocessing
* Datetime standardization
* Feature engineering
* SQL schema design
* Dashboard KPI creation
* Return and risk analytics
