from unittest.mock import patch

import numpy as np
import pandas as pd

from src.data_prep import prepare_features, split_data
from src.train import build_models, evaluate, train_all


def _synthetic_raw(n=300, seed=0):
    rng = np.random.default_rng(seed)
    signal = rng.uniform(0, 1, n)
    return pd.DataFrame(
        {
            "age": (20 + signal * 50).astype(int),
            "job": rng.choice(["admin.", "technician"], n),
            "duration": rng.integers(0, 3000, n),
            "euribor3m": rng.uniform(0.5, 5.0, n),
            # target correlated with 'signal' so models can learn something
            "y": np.where(signal + rng.normal(0, 0.3, n) > 0.8, "yes", "no"),
        }
    )


def test_build_models_returns_both_models():
    models = build_models()
    assert set(models) == {"logistic_regression", "hist_gradient_boosting"}


def test_evaluate_returns_expected_metrics():
    df = _synthetic_raw()
    X, y = prepare_features(df)
    X_train, X_test, y_train, y_test = split_data(X, y)

    model = build_models()["logistic_regression"]
    model.fit(X_train, y_train)
    metrics = evaluate(model, X_test, y_test)

    assert set(metrics) == {"roc_auc", "pr_auc", "recall", "precision"}
    assert 0.0 <= metrics["roc_auc"] <= 1.0


@patch("src.train.load_data")
def test_train_all_end_to_end_on_synthetic_data(load_data_mock):
    """Full pipeline runs without the real dataset."""
    load_data_mock.return_value = _synthetic_raw()

    results = train_all(drop_leaky=True)

    assert set(results) == {"logistic_regression", "hist_gradient_boosting"}
    for metrics in results.values():
        # Learnable synthetic signal: better than random ranking
        assert metrics["roc_auc"] > 0.5
