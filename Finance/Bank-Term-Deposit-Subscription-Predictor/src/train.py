"""Train and evaluate term-deposit subscription models.

Usage:
    python -m src.train
"""

import json
from pathlib import Path

from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    average_precision_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from src.data_prep import load_data, prepare_features, split_data

METRICS_PATH = Path(__file__).parent.parent / "metrics.json"


def build_models() -> dict:
    """Two models: interpretable baseline + gradient boosting.

    class_weight='balanced' compensates the ~9:1 class imbalance.
    """
    return {
        "logistic_regression": make_pipeline(
            StandardScaler(),
            LogisticRegression(class_weight="balanced", max_iter=2000),
        ),
        "hist_gradient_boosting": HistGradientBoostingClassifier(
            class_weight="balanced", random_state=42
        ),
    }


def evaluate(model, X_test, y_test) -> dict:
    """Ranking metrics (AUC) plus operating-point metrics at threshold 0.5."""
    proba = model.predict_proba(X_test)[:, 1]
    pred = (proba >= 0.5).astype(int)
    return {
        "roc_auc": round(roc_auc_score(y_test, proba), 4),
        "pr_auc": round(average_precision_score(y_test, proba), 4),
        "recall": round(recall_score(y_test, pred), 4),
        "precision": round(precision_score(y_test, pred), 4),
    }


def train_all(drop_leaky: bool = True) -> dict:
    """Train every model and return their test metrics."""
    df = load_data()
    X, y = prepare_features(df, drop_leaky=drop_leaky)
    X_train, X_test, y_train, y_test = split_data(X, y)

    results = {}
    for name, model in build_models().items():
        model.fit(X_train, y_train)
        results[name] = evaluate(model, X_test, y_test)
    return results


if __name__ == "__main__":
    all_results = {
        "without_duration_leakage": train_all(drop_leaky=True),
        "with_duration_leakage_do_not_use": train_all(drop_leaky=False),
    }
    METRICS_PATH.write_text(json.dumps(all_results, indent=2))
    print(json.dumps(all_results, indent=2))
