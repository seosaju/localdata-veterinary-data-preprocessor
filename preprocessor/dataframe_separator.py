import numpy as np
import pandas as pd


def have_coordinate(df: pd.DataFrame, x_column: str, y_column: str) -> pd.DataFrame:
    return df[(df[x_column].notnull()) & (df[y_column].notnull())]


def empty_coordinate(df: pd.DataFrame, x_column: str, y_column: str) -> pd.DataFrame:
    return df[(df[x_column].isnull()) | (df[y_column].isnull())]


def have_road_address(df: pd.DataFrame) -> pd.DataFrame:
    return df[df['ADDRESS'].notnull()]


def empty_road_address(df: pd.DataFrame) -> pd.DataFrame:
    return df[df['ADDRESS'].isnull()]


# 영업중
def open_hospital(df: pd.DataFrame) -> pd.DataFrame:
    return df[df["영업상태구분코드"] == 1]


# 휴업
def suspended_hospital(df: pd.DataFrame) -> pd.DataFrame:
    return df[df["영업상태구분코드"] == 2]


# 폐업, 말소
def closed_hospital(df: pd.DataFrame) -> pd.DataFrame:
    return df[df["영업상태구분코드"].isin([3, 4])]

