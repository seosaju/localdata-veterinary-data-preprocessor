import pandas as pd


def transform_date(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    df[column_name] = pd.to_datetime(df[column_name], errors='coerce').dt.strftime('%Y-%m-%d')
    return df
