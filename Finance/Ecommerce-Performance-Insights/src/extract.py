import pandas as pd
import requests

def extract(csv_folder, csv_table_mapping, public_holidays_url, year):
    dfs = {}
    for i in csv_table_mapping:
        dfs[csv_table_mapping[i]] = pd.read_csv(csv_folder / i)
    dfs["public_holidays"] = get_public_holidays(public_holidays_url, year)
    return dfs

def get_public_holidays(url, year):
    url = f"{url}/{year}/BR/"
    df_data = requests.get(url)
    df = pd.DataFrame(df_data.json())
    df["date"]= pd.to_datetime(df["date"])
    return df