import pandas as pd
from pyproj import Proj, Transformer


def transform_coordinate_system(df: pd.DataFrame, x_column: str, y_column: str,
                                old_system: str, new_system: str) -> pd.DataFrame:
    """
    translate coordinate from EPSG:2097 (Bessel 1841) to EPSG:4326 (WGS 84)
    x_column: column name of x
    y_column: column name of y
    old_system, new_system: example) 'EPSG:4326', 'EPSG:5179' ...
    :return: pandas DataFrame
    """

    old_proj = Proj(old_system)
    new_proj = Proj(new_system)

    df = __transform_coordinate(df, x_column, y_column, old_proj, new_proj)

    return df


def __transform_coordinate(df: pd.DataFrame, x_column: str, y_column: str,
                           old_proj: Proj, new_proj: Proj) -> pd.DataFrame:
    transformer = Transformer.from_proj(old_proj, new_proj, skip_equivalent=True, always_xy=True)

    converted = transformer.transform(df[x_column].values, df[y_column].values)

    df[x_column] = converted[0]
    df[y_column] = converted[1]

    return df
