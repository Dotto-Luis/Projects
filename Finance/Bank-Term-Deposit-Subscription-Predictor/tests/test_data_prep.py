import numpy as np
import pandas as pd
import pytest

from src.data_prep import prepare_features, split_data


@pytest.fixture
def raw_df():
    """Synthetic dataframe mimicking the UCI Bank Marketing schema."""
    rng = np.random.default_rng(42)
    n = 100
    return pd.DataFrame(
        {
            "age": rng.integers(18, 90, n),
            "job": rng.choice(["admin.", "technician", "student"], n),
            "marital": rng.choice(["married", "single"], n),
            "duration": rng.integers(0, 3000, n),
            "campaign": rng.integers(1, 10, n),
            "euribor3m": rng.uniform(0.5, 5.0, n),
            "y": rng.choice(["yes", "no"], n, p=[0.15, 0.85]),
        }
    )


def test_prepare_features_maps_target(raw_df):
    X, y = prepare_features(raw_df)
    assert set(y.unique()) <= {0, 1}
    assert y.sum() == (raw_df["y"] == "yes").sum()


def test_prepare_features_drops_leaky_column(raw_df):
    X, _ = prepare_features(raw_df, drop_leaky=True)
    assert "duration" not in X.columns


def test_prepare_features_can_keep_leaky_column(raw_df):
    X, _ = prepare_features(raw_df, drop_leaky=False)
    assert "duration" in X.columns


def test_prepare_features_encodes_categoricals(raw_df):
    X, _ = prepare_features(raw_df)
    # No object columns remain; dummies created for job/marital
    assert X.select_dtypes(include="object").empty
    assert any(c.startswith("job_") for c in X.columns)


def test_split_data_is_stratified(raw_df):
    X, y = prepare_features(raw_df)
    X_train, X_test, y_train, y_test = split_data(X, y, test_size=0.2)

    assert len(X_train) + len(X_test) == len(X)
    # Stratification keeps the positive rate similar in both splits
    assert abs(y_train.mean() - y_test.mean()) < 0.1
