import pytest
from sqlalchemy import create_engine, text
from pandas import DataFrame
from src.load import load

@pytest.fixture
def database():
    """Create an in-memory SQLite database and return the engine."""
    engine = create_engine('sqlite:///:memory:')
    return engine

def test_load_function(database):
    """Test the `load` function to ensure it loads dataframes correctly."""
    # Create a sample DataFrame
    df = DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

    # Create a dictionary of DataFrames
    data_frames = {'example_table': df}

    # Call the load function
    load(data_frames=data_frames, database=database)

    # Verify the data was loaded correctly
    with database.connect() as connection:
        result = connection.execute(text("SELECT * FROM example_table")).fetchall()
        assert result == [(1, 4), (2, 5), (3, 6)]
