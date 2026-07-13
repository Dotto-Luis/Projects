from pathlib import Path
from typing import Tuple

import pandas as pd
from sklearn.model_selection import train_test_split

DATA_PATH = Path(__file__).parent.parent / "data" / "bank-additional-full.csv"

# 'duration' is the call duration in seconds. It is only known AFTER the call
# ends — at prediction time (deciding whom to call) it does not exist. Using it
# inflates metrics dramatically and makes the model useless in production
# (classic data leakage, documented by the UCI dataset authors).
LEAKY_COLUMNS = ["duration"]

TARGET = "y"


def load_data(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load the UCI Bank Marketing dataset (semicolon-separated)."""
    return pd.read_csv(path, sep=";")


def prepare_features(
    df: pd.DataFrame, drop_leaky: bool = True
) -> Tuple[pd.DataFrame, pd.Series]:
    """
    Turn the raw dataframe into a model-ready feature matrix and binary target.

    - Maps the target 'y' (yes/no) to 1/0.
    - Optionally drops leakage-prone columns (see LEAKY_COLUMNS).
    - One-hot encodes categorical features (drop_first to avoid redundancy).
    """
    df = df.copy()
    y = (df[TARGET] == "yes").astype(int)
    X = df.drop(columns=[TARGET])

    if drop_leaky:
        X = X.drop(columns=[c for c in LEAKY_COLUMNS if c in X.columns])

    X = pd.get_dummies(X, drop_first=True)
    return X, y


def split_data(
    X: pd.DataFrame, y: pd.Series, test_size: float = 0.2, random_state: int = 42
):
    """Stratified train/test split (the target is imbalanced: ~11% positives)."""
    return train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
