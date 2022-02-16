import pandas as pd


def read_dataframe(file_path: str, encoding: str) -> pd.DataFrame:
    df = pd.read_csv(file_path, encoding=encoding)   # read csv file
    df = df.reset_index(drop=True)  # drop index column
    return df
