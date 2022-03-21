import pandas as pd


def read_dataframe(file_path: str, sheet_name: str) -> pd.DataFrame:
    df = pd.read_excel(file_path, sheet_name=sheet_name, engine="openpyxl")  # read csv file
    df = df.reset_index(drop=True)  # drop index column
    return df
