from typing import Dict
import pandas as pd

import requests
from pandas import DataFrame, read_csv, read_json, to_datetime

public_holidays_url = 'https://date.nager.at/api/v3/PublicHolidays'

def get_public_holidays(public_holidays_url: str, year: str) -> DataFrame:
    url = f'{public_holidays_url}/{year}/BR'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        holidays_df = DataFrame(data)
        holidays_df['date'] = to_datetime(holidays_df['date'])
        holidays_df = holidays_df.drop(columns=['types', 'counties'])

        return holidays_df
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        raise SystemExit
    
csv_folder = r'C:\Users\n600\Documents\ML-Projects\AnyoneAI-SprintI\dataset'

def extract(csv_folder: str, csv_table_mapping: Dict[str, str], public_holidays_url: str) -> Dict[str, DataFrame]:
    dataframes = {table_name: read_csv(f"{csv_folder}/{csv_file}")
        for csv_file, table_name in csv_table_mapping.items()}
    holidays = get_public_holidays(public_holidays_url, "2016")
    holidays = get_public_holidays(public_holidays_url, "2017")
    holidays = get_public_holidays(public_holidays_url, "2018")
    dataframes["public_holidays"] = holidays

    return dataframes


holidays_2016 = get_public_holidays(public_holidays_url, "2016")
holidays_2017 = get_public_holidays(public_holidays_url, "2017")
holidays_2018 = get_public_holidays(public_holidays_url, "2018")

holidaysBR = pd.concat([holidays_2016, holidays_2017, holidays_2018])
