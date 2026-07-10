from unittest.mock import patch

import pandas as pd

from src.data_utils import get_datasets, get_feature_target, get_train_val_sets


@patch("src.data_utils.pd.read_csv")
@patch("src.data_utils.gdown.download")
@patch("src.data_utils.os.path.exists", return_value=False)
def test_get_datasets(exists_mock, download_mock, read_csv_mock, app_train):
    """get_datasets downloads missing files and loads the three dataframes."""
    read_csv_mock.return_value = app_train

    train, test, description = get_datasets()

    # One download per missing file: train, test, columns description
    assert download_mock.call_count == 3
    assert isinstance(train, pd.DataFrame)
    assert isinstance(test, pd.DataFrame)
    assert isinstance(description, pd.DataFrame)


def test_get_feature_target(app_train: pd.DataFrame, app_test: pd.DataFrame):
    """TARGET is separated from features in both datasets."""
    X_train, y_train, X_test, y_test = get_feature_target(app_train, app_test)

    assert isinstance(X_train, pd.DataFrame)
    assert isinstance(X_test, pd.DataFrame)
    assert "TARGET" not in X_train.columns
    assert "TARGET" not in X_test.columns
    assert X_train.shape == (len(app_train), app_train.shape[1] - 1)
    assert X_test.shape == (len(app_test), app_test.shape[1] - 1)
    assert y_train.shape == (len(app_train),)
    assert y_test.shape == (len(app_test),)


def test_get_train_val_sets(app_train: pd.DataFrame, app_test: pd.DataFrame):
    """Train/validation split is 80/20, reproducible, and loses no rows."""
    X, y, _, _ = get_feature_target(app_train, app_test)
    X_train, X_val, y_train, y_val = get_train_val_sets(X, y)

    assert isinstance(X_train, pd.DataFrame)
    assert len(X_train) + len(X_val) == len(X)
    assert len(X_val) == round(0.2 * len(X))
    assert len(X_train) == len(y_train)
    assert len(X_val) == len(y_val)

    # Reproducibility: same seed -> same split
    X_train2, _, _, _ = get_train_val_sets(X, y)
    pd.testing.assert_frame_equal(X_train, X_train2)
