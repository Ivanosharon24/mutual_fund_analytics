-- =====================================================
-- TOP 5 FUNDS BY AUM
-- =====================================================

SELECT
    scheme_name,
    fund_house,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- =====================================================
-- AVERAGE NAV BY FUND
-- =====================================================

SELECT
    amfi_code,
    ROUND(AVG(nav), 2) AS avg_nav
FROM fact_nav
GROUP BY amfi_code
ORDER BY avg_nav DESC;

-- =====================================================
-- TOTAL TRANSACTION AMOUNT BY STATE
-- =====================================================

SELECT
    state,
    ROUND(SUM(amount_inr), 2) AS total_transaction_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_transaction_amount DESC;

-- =====================================================
-- TRANSACTION COUNT BY TYPE
-- =====================================================

SELECT
    transaction_type,
    COUNT(*) AS transaction_count
FROM fact_transactions
GROUP BY transaction_type
ORDER BY transaction_count DESC;

-- =====================================================
-- FUNDS WITH EXPENSE RATIO < 1%
-- =====================================================

SELECT
    amfi_code,
    return_3yr_pct,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY return_3yr_pct DESC;

-- =====================================================
-- AVERAGE 3-YEAR RETURNS BY CATEGORY
-- =====================================================

SELECT
    category,
    ROUND(AVG(return_3yr_pct), 2) AS avg_3yr_return
FROM fact_performance
GROUP BY category
ORDER BY avg_3yr_return DESC;

-- =====================================================
-- TOP STATES BY INVESTMENT AMOUNT
-- =====================================================

SELECT
    state,
    ROUND(SUM(amount_inr), 2) AS total_investment
FROM fact_transactions
GROUP BY state
ORDER BY total_investment DESC
LIMIT 10;

-- =====================================================
-- PAYMENT MODE DISTRIBUTION
-- =====================================================

SELECT
    payment_mode,
    COUNT(*) AS usage_count
FROM fact_transactions
GROUP BY payment_mode
ORDER BY usage_count DESC;

-- =====================================================
-- AVERAGE RETURNS VS BENCHMARK
-- =====================================================

SELECT
    ROUND(AVG(return_3yr_pct), 2) AS avg_fund_return,
    ROUND(AVG(benchmark_3yr_pct), 2) AS avg_benchmark_return
FROM fact_performance;

-- =====================================================
-- RISK CATEGORY DISTRIBUTION
-- =====================================================

SELECT
    risk_category,
    COUNT(*) AS fund_count
FROM dim_fund
GROUP BY risk_category
ORDER BY fund_count DESC;