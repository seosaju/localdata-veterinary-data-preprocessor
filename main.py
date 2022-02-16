import logging

import pandas as pd

from preprocessor import subset_manager, coordinate_translator
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

    logging.info('save result.csv file')
    df.to_csv("data/result.csv", na_rep='', encoding='cp949')
