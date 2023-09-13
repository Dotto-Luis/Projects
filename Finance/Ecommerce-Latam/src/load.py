from typing import Dict

from pandas import DataFrame
from sqlalchemy.engine.base import Engine


def load(data_frames: Dict[str, DataFrame], database: Engine):
    """Load the dataframes into the sqlite database.

    Args:
        data_frames (Dict[str, DataFrame]): A dictionary with keys as the table names
        and values as the dataframes.
    """
    # TODO: Implement this function. For each dataframe in the dictionary, you must
    # use pandas.Dataframe.to_sql() to load the dataframe into the database as a
    # table.
    # For the table name use the `data_frames` dict keys.
    import pandas as pd
    import os
    csv_folder = 'C:/Users/n600/Documents/ML-Projects/AnyoneAI-SprintI/assignment/dataset/'
    dataframes_dict = {}
    file_list = os.listdir(csv_folder)
    while file_list:
        csv_filename = file_list.pop(0)
        if csv_filename.endswith('.csv'):
            csv_name = os.path.splitext(csv_filename)[0]
            csv_path = os.path.join(csv_folder, csv_filename)
            df = pd.read_csv(csv_path)
            dataframes_dict[csv_name] = df
    raise NotImplementedError


