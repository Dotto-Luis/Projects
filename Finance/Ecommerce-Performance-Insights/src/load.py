from sqlalchemy.engine import Engine
import pandas as pd
from sqlalchemy import text

def load(data_frames: dict, database: Engine):
    """Load dataframes into the specified database."""
    with database.connect() as connection:
        for key, df in data_frames.items():
            df.to_sql(name=key, con=connection, if_exists="replace", index=False)
