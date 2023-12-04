from typing import List, Optional, Tuple, Union

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.base import BaseEstimator
from sklearn.preprocessing import label_binarize


def get_performance(
    predictions: Union[List, np.ndarray],
    y_test: Union[List, np.ndarray],
    labels: Optional[Union[List, np.ndarray]] = [1, 0],
) -> Tuple[float, float, float, float]:
    """
    Get model performance using different metrics.

    Args:
        predictions : Union[List, np.ndarray]
            Predicted labels, as returned by a classifier.
        y_test : Union[List, np.ndarray]
            Ground truth (correct) labels.
        labels : Union[List, np.ndarray]
            Optional display names matching the labels (same order).
            Used in `classification_report()`.

    Return:
        accuracy : float
        precision : float
        recall : float
        f1_score : float
    """
    # TODO: Compute metrics
    # Use sklearn.metrics.accuracy_score
    accuracy = ...
    # Use sklearn.metrics.precision_score
    precision = ...
    # Use sklearn.metrics.recall_score
    recall = ...
    # Use sklearn.metrics.f1_score
    f1_score = ...
    # Use sklearn.metrics.classification_report
    report = ...

    # TODO: Get Confusion Matrix, use sklearn.metrics.confusion_matrix
    cm = ...

    # Convert Confusion Matrix to pandas DataFrame, don't change this code!
    cm_as_dataframe = pd.DataFrame(data=cm)
    # Print metrics, don't change this code!
    print("Model Performance metrics:")
    print("-" * 30)
    print("Accuracy:", accuracy)
    print("Precision:", precision)
    print("Recall:", recall)
    print("F1 Score:", f1_score)
    print("\nModel Classification report:")
    print("-" * 30)
    print(report)
    print("\nPrediction Confusion Matrix:")
    print("-" * 30)
    print(cm_as_dataframe)

    # Return resulting metrics, don't change this code!
    return accuracy, precision, recall, f1_score


def plot_roc(
    model: BaseEstimator, y_test: Union[List, np.ndarray], features: np.ndarray
) -> float:
    """
    Plot ROC Curve graph.

    Args:
        model : BaseEstimator
            Classifier model.
        y_test : Union[List, np.ndarray]
            Ground truth (correct) labels.
        features : List[int]
            Dataset features used to evaluate the model.

    Return:
        roc_auc : float
            ROC AUC Score.
    """
    fpr = dict()
    tpr = dict()
    roc_auc = dict()
    class_labels = model.classes_
    y_test = label_binarize(y_test, classes=class_labels)

    prob = model.predict_proba(features)
    y_score = prob[:, prob.shape[1] - 1]

    fpr, tpr, _ = metrics.roc_curve(y_test, y_score)
    roc_auc = metrics.auc(fpr, tpr)

    plt.figure(figsize=(10, 5))
    plt.plot(fpr, tpr, label=f"ROC curve (area = {roc_auc})", linewidth=2.5)
    plt.plot([0, 1], [0, 1], "k--")
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("Receiver Operating Characteristic (ROC) Curve")
    plt.legend(loc="lower right")
    plt.show()

    return roc_auc
