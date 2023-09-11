import pandas as pd
from typing import Dict
import os
from pandas import DataFrame
from sqlalchemy.engine.base import Engine


def load(data_frames: Dict[str, DataFrame], database: Engine):
    for table_name, df in data_frames.items():
        # Use pandas to_sql() method to load the DataFrame into the database
        df.to_sql(table_name, con=database, if_exists='replace', index=False)

if __name__ == "__main__":


    # Define the folder containing the CSV files\
    csv_folder = r'C:\Users\n600\Documents\ML-Projects\AnyoneAI-SprintI\assignment\dataset'

    # Initialize an empty dictionary to store DataFrames
    data_frames = {}

    # Load each CSV file into a DataFrame and store it in the dictionary
    for i in range(1, 10):
        csv_file = os.path.join(csv_folder, f'csv{i}.csv')
        table_name = f'dataset{i}'
        data_frames[table_name] = pd.read_csv(csv_file)

    # Assuming you have generated a DataFrame named 'data_frame' in 'extract.py'
    # Add 'data_frame' to the dictionary with a desired table name
    data_frames['custom_table_name'] = data_frame

    # Create a SQLAlchemy engine for your database
    database_url = 'your_database_connection_url_here'
    database = create_engine(database_url)

    # Call the function to load the DataFrames into the database
    load_dataframes_to_database(data_frames, database)



