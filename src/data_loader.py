# src/data_loader.py

import pandas as pd

# These are the five financial product types we're interested in
TARGET_PRODUCTS = [
    "Credit card",
    "Personal loan",
    "Buy Now, Pay Later",
    "Savings account",
    "Money transfers"
]

def load_raw_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    print(f"Loaded {len(df)} rows.")
    return df

def filter_target_products(df: pd.DataFrame) -> pd.DataFrame:
    filtered = df[df["Product"].isin(TARGET_PRODUCTS)]
    print(f"Filtered to {len(filtered)} rows across target products.")
    return filtered

def remove_empty_narratives(df: pd.DataFrame) -> pd.DataFrame:
    df = df[df["Consumer complaint narrative"].notna()]
    df = df[df["Consumer complaint narrative"].str.strip() != ""]
    print(f"{len(df)} rows remaining after removing empty narratives.")
    return df
