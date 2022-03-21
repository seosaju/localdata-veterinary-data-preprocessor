import numpy as np
import pandas as pd


def transform_to_text(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    df[column_name] = df[column_name].astype(str)
    return df


def fit_to_zip_code(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    df[column_name] = df[column_name].fillna(0)
    df[column_name] = df[column_name].astype(int)
    df[column_name] = df[column_name].astype(str)

    for i, zipcode in enumerate(df[column_name]):
        if zipcode == "0":
            df[column_name].iloc[i] = np.NAN
        elif len(zipcode) == 4:
            df[column_name].iloc[i] = "0" + zipcode

    return df
