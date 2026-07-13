import pandas as pd

from src.utils.data_loader import load_loan_data
from src.utils.data_summary import create_data_summary


def test_load_loan_data(tmp_path):
    """Loader reads a CSV into a DataFrame."""
    csv = tmp_path / "loans.csv"
    csv.write_text("Loan_ID,Amount\nLP1,100\nLP2,200\n")

    df = load_loan_data(str(csv))

    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)
    assert list(df.columns) == ["Loan_ID", "Amount"]


def test_create_data_summary():
    """Summary includes shape and every column with its dtype."""
    df = pd.DataFrame({"name": ["a", "b"], "amount": [1.5, 2.5]})

    summary = create_data_summary(df)

    assert "2 rows and 2 columns" in summary
    assert "name" in summary
    assert "amount" in summary
    assert "float64" in summary
