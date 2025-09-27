# src/utils/data_summary.py

def create_data_summary(df):
    summary = f"The dataset has {df.shape[0]} rows and {df.shape[1]} columns.\n"
    summary += "Columns:\n"
    for col in df.columns:
        summary += f"- {col} (type: {df[col].dtype})\n"
    return summary
