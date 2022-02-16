import pandas as pd


# 영업중
def open_hospital(df: pd.DataFrame) -> pd.DataFrame:
    return df[df["영업상태구분코드"] == 1]


# 휴업
def suspended_hospital(df: pd.DataFrame) -> pd.DataFrame:
    return df[df["영업상태구분코드"] == 2]


# 폐업, 말소
def closed_hospital(df: pd.DataFrame) -> pd.DataFrame:
    return df[df["영업상태구분코드"].isin([3, 4])]


def have_essential_data(df: pd.DataFrame, x_column: str, y_column: str, address: str) -> pd.DataFrame:
    return (df[x_column].notnull()) & (df[y_column].notnull()) & (df[address].notnull())
