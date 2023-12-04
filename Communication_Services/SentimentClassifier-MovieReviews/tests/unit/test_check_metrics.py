from pathlib import Path

import pandas as pd
from sklearn import metrics

from src import config, evaluation


def test_get_performance():
    accuracy, precision, recall, f1_score = evaluation.get_performance(
        [1, 1, 1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 1, 1, 0, 0, 0]
    )

    assert accuracy == 0.6, "You must check your get_performance function!"
    assert precision == 0.6, "You must check your get_performance function!"
    assert recall == 0.6, "You must check your get_performance function!"
    assert f1_score == 0.6, "You must check your get_performance function!"


def test_best_model():
    DATASET_TEST_PREDICT = str(
        Path(config.DATASET_ROOT_PATH) / "movies_review_predict_aai.csv"
    )
    app_test = pd.read_csv(config.DATASET_TEST)

    app_test_predict = pd.read_csv(DATASET_TEST_PREDICT)

    roc_auc = metrics.roc_auc_score(
        y_true=app_test["positive"], y_score=app_test_predict["positive"]
    )

    assert roc_auc > 0.85, "Your best model is not good enough!"
