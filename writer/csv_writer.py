import pandas as pd


def save_csv(df: pd.DataFrame, path: str, filename: str) -> None:
    df.to_csv(f'data/{path}/{filename}.csv', na_rep='', encoding='cp949', index=False)