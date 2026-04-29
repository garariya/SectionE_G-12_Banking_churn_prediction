# Banking Churn Analysis


## Project Overview

Customer churn is a major challenge in the banking industry because retaining existing customers is significantly more cost-effective than acquiring new ones. This project analyzes banking customer behavior to identify churn patterns, understand key risk factors, and generate actionable business insights using Python and Tableau.

The project follows a complete analytics workflow including data cleaning, exploratory data analysis, statistical testing, KPI generation, and interactive dashboard development.

---

## Project Structure
- data/raw → original dataset
- data/processed → cleaned data
- notebooks → analysis workflow
- scripts → ETL pipeline
- tableau → dashboards
- reports → final outputs

## KPIs
- Customer Churn Rate
- Customer Retention Rate


## Objectives

- Analyze customer churn behavior
- Identify factors influencing churn
- Prepare a clean analytical dataset
- Generate business KPIs
- Build an interactive Tableau dashboard
- Provide retention recommendations

---

## Dataset Summary

- **Total Records:** 28,382 customers  
- **Features:** 20+ columns  
- **Target Variable:** `churn`

Where:

- `0` = Retained Customer  
- `1` = Churned Customer

### Main Variables

- Age
- Gender
- Occupation
- Dependents
- Current Balance
- Monthly Credit / Debit
- Previous Balance
- Customer Tenure
- Net Worth Category
- Last Transaction
- Churn

---

## Project Structure

```text
SectionName_TeamID_ProjectName/
│── README.md
│── data/
│   ├── raw/
│   └── processed/
│
│── notebooks/
│   ├── 01_extraction.ipynb
│   ├── 02_cleaning.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_statistical_analysis.ipynb
│   └── 05_final_load_prep.ipynb
│
│── scripts/
│   └── etl_pipeline.py
│
│── tableau/
│   ├── screenshots/
│   └── dashboard_links.md
│
│── reports/
│   ├── project_report.pdf
│   └── presentation.pdf
│
│── docs/
│   └── data_dictionary.md