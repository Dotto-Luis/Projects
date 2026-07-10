import numpy as np
import pandas as pd

from src.data_utils import get_feature_target, get_train_val_sets
from src.preprocessing import preprocess_data


def test_preprocess_data(app_train: pd.DataFrame, app_test: pd.DataFrame):
    """Full preprocessing: encoding, imputation, and scaling."""
    X_train, y_train, X_test, _ = get_feature_target(app_train, app_test)
    X_train, X_val, y_train, _ = get_train_val_sets(X_train, y_train)

    train_data, val_data, test_data = preprocess_data(X_train, X_val, X_test)

    # Output types and row counts preserved
    assert isinstance(train_data, np.ndarray)
    assert isinstance(val_data, np.ndarray)
    assert isinstance(test_data, np.ndarray)
    assert train_data.shape[0] == len(X_train)
    assert val_data.shape[0] == len(X_val)
    assert test_data.shape[0] == len(X_test)

    # Same feature space across the three sets
    assert train_data.shape[1] == val_data.shape[1] == test_data.shape[1]

    # One-hot expands multi-category columns: more columns than the input
    assert train_data.shape[1] > X_train.shape[1]

    # Imputation: no NaNs left (DAYS_EMPLOYED anomaly 365243 replaced then imputed)
    assert not np.isnan(train_data).any()
    assert not np.isnan(val_data).any()
    assert not np.isnan(test_data).any()

    # Min-Max scaling: train data within [0, 1]
    assert train_data.min() >= 0.0
    assert train_data.max() <= 1.0
