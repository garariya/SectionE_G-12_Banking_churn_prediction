# Data Dictionary

## Banking Customer Churn Dataset

This document describes all variables used in the Banking Customer Churn Analysis project.

| Column Name | Data Type | Description | Example |
|---|---|---|---|
| age | Integer | Customer age in years | 45 |
| gender | Categorical | Customer gender | Male / Female |
| dependents | Integer | Number of dependents linked to customer | 0, 2 |
| occupation | Categorical | Employment category of customer | salaried, self_employed |
| customer_nw_category | Integer | Net worth / customer value segment | 1, 2, 3 |
| current_balance | Float | Current account balance | 5400.75 |
| previous_month_end_balance | Float | Balance at previous month end | 5100.30 |
| average_monthly_balance_prevQ | Float | Average monthly balance in previous quarter | 4900.20 |
| average_monthly_balance_prevQ2 | Float | Average monthly balance in quarter before previous quarter | 4700.80 |
| current_month_credit | Float | Credit amount in current month | 1200.50 |
| previous_month_credit | Float | Credit amount in previous month | 950.40 |
| current_month_debit | Float | Debit amount in current month | 700.00 |
| previous_month_debit | Float | Debit amount in previous month | 680.00 |
| current_month_balance | Float | Current month average balance | 5200.25 |
| previous_month_balance | Float | Previous month average balance | 5050.90 |
| churn | Integer | Customer churn status | 0 / 1 |
| last_transaction | Date | Last recorded transaction date | 2019-08-15 |
| customer_tenure_years | Float | Customer relationship tenure in years (derived from vintage) | 6.28 |

---

## Encoded Variables

### churn

| Value | Meaning |
|---|---|
| 0 | Retained Customer |
| 1 | Churned Customer |

### customer_nw_category

| Value | Meaning |
|---|---|
| 1 | Low Net Worth |
| 2 | Medium Net Worth |
| 3 | High Net Worth |

---

## Removed Columns During Cleaning

| Column | Reason |
|---|---|
| city | Synthetic / arbitrary identifier |
| branch_code | Synthetic / arbitrary identifier |

---

## Derived Columns

### customer_tenure_years

Converted from:

```text
vintage (days)
```

## Removed During Cleaning

| Column | Reason |
|---|---|
| customer_id | Identifier only |
| city | Synthetic / arbitrary |
| branch_code | Synthetic / arbitrary |