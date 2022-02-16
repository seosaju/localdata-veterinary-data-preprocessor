import pandas as pd


def make_subset(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    return df[columns]


def rename_column(df: pd.DataFrame, rename_column_dict: dict) -> pd.DataFrame:
    return df.rename(columns=rename_column_dict)
