# src/utils/data_loader.py

import pandas as pd

def load_loan_data(path='data/loan_prediction.csv'):
    return pd.read_csv(path)
