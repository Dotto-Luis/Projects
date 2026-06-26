import pandas as pd
from datetime import datetime
import os

LOG_PATH = "../experiments/experiment_log.csv"

def log_experiment(
    experiment_id,
    model,
    features,
    hyperparameters,
    cv_score,
    leaderboard_score=None,
    notes=""
):
    row = {
        "experiment_id": experiment_id,
        "model": model,
        "features": features,
        "hyperparameters": hyperparameters,
        "cv_score": cv_score,
        "leaderboard_score": leaderboard_score,
        "notes": notes,
        "date": datetime.now()
    }

    df_new = pd.DataFrame([row])

    if os.path.exists(LOG_PATH):
        df = pd.read_csv(LOG_PATH)
        df = pd.concat([df, df_new], ignore_index=True)
    else:
        df = df_new

    df.to_csv(LOG_PATH, index=False)