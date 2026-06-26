import pandas as pd

def convert_orders_dates(dfs):
    for llave, valor in dfs.items():
        for feature in valor:
            if "date" in feature or "timestamp" in feature or "_at" in feature:
                dfs[llave][feature] = pd.to_datetime(dfs[llave][feature])
