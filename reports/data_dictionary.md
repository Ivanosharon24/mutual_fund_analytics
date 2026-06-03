# Data Dictionary

## 1. dim_fund

| Column        | Data Type | Description                         |
| ------------- | --------- | ----------------------------------- |
| amfi_code     | INTEGER   | Unique AMFI mutual fund scheme code |
| scheme_name   | TEXT      | Name of mutual fund scheme          |
| fund_house    | TEXT      | Asset management company            |
| category      | TEXT      | Broad mutual fund category          |
| sub_category  | TEXT      | SEBI sub-category classification    |
| plan          | TEXT      | Direct or Regular plan              |
| risk_category | TEXT      | Risk classification of fund         |

---

## 2. fact_nav

| Column    | Data Type | Description                   |
| --------- | --------- | ----------------------------- |
| amfi_code | INTEGER   | Mutual fund scheme identifier |
| nav_date  | DATE      | NAV reporting date            |
| nav       | REAL      | Net Asset Value               |

---

## 3. fact_transactions

| Column             | Data Type | Description                |
| ------------------ | --------- | -------------------------- |
| investor_id        | TEXT      | Unique investor identifier |
| transaction_date   | DATE      | Date of transaction        |
| amfi_code          | INTEGER   | Mutual fund scheme code    |
| transaction_type   | TEXT      | SIP / Lumpsum / Redemption |
| amount_inr         | REAL      | Transaction amount in INR  |
| state              | TEXT      | Investor state             |
| city               | TEXT      | Investor city              |
| city_tier          | TEXT      | Tier classification        |
| age_group          | TEXT      | Investor age segment       |
| gender             | TEXT      | Investor gender            |
| annual_income_lakh | REAL      | Annual income in lakhs     |
| payment_mode       | TEXT      | UPI / NetBanking / etc     |
| kyc_status         | TEXT      | KYC verification status    |

---

## 4. fact_performance

| Column             | Data Type | Description                      |
| ------------------ | --------- | -------------------------------- |
| amfi_code          | INTEGER   | Mutual fund scheme code          |
| return_1yr_pct     | REAL      | 1-year return percentage         |
| return_3yr_pct     | REAL      | 3-year return percentage         |
| return_5yr_pct     | REAL      | 5-year return percentage         |
| benchmark_3yr_pct  | REAL      | Benchmark return                 |
| alpha              | REAL      | Risk-adjusted excess return      |
| beta               | REAL      | Volatility vs benchmark          |
| sharpe_ratio       | REAL      | Risk-adjusted performance metric |
| sortino_ratio      | REAL      | Downside-risk adjusted return    |
| std_dev_ann_pct    | REAL      | Annualized volatility            |
| max_drawdown_pct   | REAL      | Maximum observed loss            |
| aum_crore          | REAL      | Assets under management          |
| expense_ratio_pct  | REAL      | Expense ratio percentage         |
| morningstar_rating | INTEGER   | Morningstar fund rating          |

---

## Source References

| Dataset      | Source               |
| ------------ | -------------------- |
| NAV Data     | mfapi.in             |
| Fund Master  | Internal CSV dataset |
| Transactions | Internal CSV dataset |
| Performance  | Internal CSV dataset |
