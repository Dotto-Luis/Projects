import numpy as np
import pandas as pd
from pytest import fixture

N_TRAIN = 200
N_TEST = 50


def _make_dataset(n_rows: int, seed: int) -> pd.DataFrame:
    """Build a small synthetic dataset mimicking the Home Credit schema.

    Includes the column types the pipeline must handle: a binary categorical
    (ordinal encoding), a multi-category categorical (one-hot encoding),
    numeric features with missing values, and the DAYS_EMPLOYED anomaly (365243).
    """
    rng = np.random.default_rng(seed)
    df = pd.DataFrame(
        {
            "SK_ID_CURR": np.arange(n_rows, dtype=float),
            "TARGET": rng.integers(0, 2, n_rows),
            # 2 categories -> OrdinalEncoder
            "NAME_CONTRACT_TYPE": rng.choice(
                ["Cash loans", "Revolving loans"], n_rows
            ),
            "FLAG_OWN_CAR": rng.choice(["Y", "N"], n_rows),
            # >2 categories -> OneHotEncoder
            "OCCUPATION_TYPE": rng.choice(
                ["Laborers", "Core staff", "Managers", "Drivers"], n_rows
            ),
            # numeric features
            "AMT_INCOME_TOTAL": rng.uniform(25_000, 300_000, n_rows),
            "DAYS_EMPLOYED": rng.choice([-2000.0, -500.0, 365243.0], n_rows),
        }
    )
    # Inject missing values to exercise the imputer
    missing_idx = df.sample(frac=0.1, random_state=seed).index
    df.loc[missing_idx, "AMT_INCOME_TOTAL"] = np.nan
    return df


@fixture(scope="session")
def app_train() -> pd.DataFrame:
    """Synthetic train dataset (no download required)."""
    return _make_dataset(N_TRAIN, seed=42)


@fixture(scope="session")
def app_test() -> pd.DataFrame:
    """Synthetic test dataset (no download required)."""
    return _make_dataset(N_TEST, seed=7)
