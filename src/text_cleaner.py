# src/text_cleaner.py

import pandas as pd
import re

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def apply_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["cleaned_narrative"] = df["Consumer complaint narrative"].apply(clean_text)
    return df
  
