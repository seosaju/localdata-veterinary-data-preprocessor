import logging

import numpy as np
import pandas as pd

from preprocessor import subset_manager, coordinate_translator, dataframe_separator
from reader import csv_reader

column_list = ['번호', '관리번호', '영업상태구분코드', '영업상태명', '상세영업상태코드', '상세영업상태명',
               '소재지우편번호', '소재지전체주소', '도로명전체주소', '도로명우편번호', '사업장명',
               '데이터갱신일자', '좌표정보(x)', '좌표정보(y)']

x_column = 'LONGITUDE'
y_column = 'LATITUDE'

rename_column_dict = {'관리번호': 'MANAGEMENT_NUMBER',
                      '사업장명': 'NAME',
                      '도로명전체주소': 'ADDRESS',
                      '도로명우편번호': 'ZIP_CODE',
                      '소재지전체주소': 'SUB_ADDRESS',
                      '소재지우편번호': 'SUB_ZIPCODE',
                      '좌표정보(x)': x_column,
                      '좌표정보(y)': y_column}

logging.basicConfig(
    format='%(asctime)s:%(levelname)s:%(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.INFO)


def create_csv_files(df: pd.DataFrame, x: str, y: str, path: str) -> None:
    have_xy = dataframe_separator.have_coordinate(df, x, y)
    save_csv(dataframe_separator.have_road_address(have_xy), path, path + '-좌표O-도로명주소O')
    save_csv(dataframe_separator.empty_road_address(have_xy), path, path + '-좌표O-도로명주소X')

    not_have_xy = dataframe_separator.empty_coordinate(df, x, y)
    save_csv(dataframe_separator.have_road_address(not_have_xy), path, path + '-좌표X-도로명주소O')
    save_csv(dataframe_separator.empty_road_address(not_have_xy), path, path + '-좌표X-도로명주소X')


def save_csv(df: pd.DataFrame, path: str, filename: str) -> None:
    df.to_csv(f'data/{path}/{filename}.csv', na_rep='', encoding='cp949', index=False)


if __name__ == "__main__":
    df: pd.DataFrame

    # read csv file
    logging.info("Read .csv file")
    df = csv_reader.read_dataframe("data/data.csv", encoding='cp949')

    # preprocessing
    logging.info("Preprocessing pandas dataframe")
    df = subset_manager.make_subset(df, column_list)
    logging.info('Rename column')
    df = subset_manager.rename_column(df, rename_column_dict)
    logging.info('transform coordinate system')
    df = coordinate_translator.transform_coordinate_system(df, x_column, y_column, 'EPSG:2097', 'EPSG:4326')

    # replace coordinate inf to nan
    df = df.replace(np.inf, np.nan)

    logging.info('separate data frame')

    # 영업중
    opened_df = dataframe_separator.open_hospital(df)
    logging.info('영업중인 병원 .csv 저장')
    create_csv_files(opened_df, x_column, y_column, "영업중")

    # 휴업중
    suspended_df = dataframe_separator.suspended_hospital(df)
    logging.info('휴업중인 병원 .csv 저장')
    create_csv_files(suspended_df, x_column, y_column, "휴업중")

    # 폐업, 말소
    closed_df = dataframe_separator.closed_hospital(df)
    logging.info('폐업-말소된 병원 .csv 저장')
    create_csv_files(closed_df, x_column, y_column, "폐업-말소")
