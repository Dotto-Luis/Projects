from typing import Dict

from pandas import DataFrame
from sqlalchemy.engine.base import Engine


def load(data_frames: Dict[str, DataFrame], database: Engine):
    """Load the dataframes into the sqlite database.

    Args:
        data_frames (Dict[str, DataFrame]): A dictionary with keys as the table names
        and values as the dataframes.
    """

    with database.begin() as connection:
        for key, value in data_frames.items():
            df_sql = value
            df_sql.to_sql(key, connection, if_exists="replace", index=False)

    # raise NotImplementedError
