import pandas as pd
import numpy as np

# -----------------------------
# EXTRACT
# -----------------------------
def extract_data(path):
    print("Loading raw dataset...")
    df = pd.read_csv("../data/raw/Banking_churn_prediction.csv")
    return df


# -----------------------------
# TRANSFORM
# -----------------------------
def clean_data(df):

    print("Starting cleaning process...")

    # Convert date column
    df["last_transaction"] = pd.to_datetime(
        df["last_transaction"], errors="coerce"
    )

    # Fill missing values
    df["gender"].fillna(df["gender"].mode()[0], inplace=True)
    df["occupation"].fillna(df["occupation"].mode()[0], inplace=True)
    df["dependents"].fillna(df["dependents"].median(), inplace=True)

    # Convert datatypes
    df["dependents"] = df["dependents"].astype(int)

    # Handle unrealistic dependents
    median_dep = int(df.loc[df["dependents"] <= 9, "dependents"].median())
    df.loc[df["dependents"] > 9, "dependents"] = median_dep

    # Convert vintage days to years
    df["customer_tenure_years"] = round(df["vintage"] / 365, 2)

    # Drop synthetic columns
    drop_cols = ["city", "branch_code"]
    df.drop(columns=drop_cols, inplace=True, errors="ignore")

    print("Cleaning completed.")

    return df


# -----------------------------
# LOAD
# -----------------------------
def load_data(df, path):
    df.to_csv(path, index=False)
    print(f"Processed data saved to {path}")


# -----------------------------
# MAIN PIPELINE
# -----------------------------
def run_pipeline():

    input_path = "data/raw/bank_churn.csv"
    output_path = "data/processed/cleaned_banking_churn.csv"

    df = extract_data(input_path)
    df_clean = clean_data(df)
    load_data(df_clean, output_path)


if __name__ == "__main__":
    run_pipeline()