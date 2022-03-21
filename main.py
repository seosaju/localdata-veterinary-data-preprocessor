import logging

import numpy as np
import pandas as pd

from preprocessor import subset_manager, coordinate_translator, dataframe_separator, date_transformer
from reader import csv_reader
from writer import csv_writer

column_list = ['번호', '관리번호', '영업상태구분코드', '영업상태명', '상세영업상태코드', '상세영업상태명',
               '소재지우편번호', '소재지전체주소', '소재지전화', '도로명전체주소', '도로명우편번호', '사업장명',
               '데이터갱신일자', '좌표정보(X)', '좌표정보(Y)']

x_column = 'LONGITUDE'
y_column = 'LATITUDE'
address = 'ADDRESS'

rename_column_dict = {'관리번호': 'MANAGEMENT_NUMBER',
                      '사업장명': 'NAME',
                      '도로명전체주소': address,
                      '도로명우편번호': 'ZIP_CODE',
                      '소재지전체주소': 'SUB_ADDRESS',
                      '소재지우편번호': 'SUB_ZIPCODE',
                      '소재지전화': 'PHONE_NUMBER',
                      '좌표정보(X)': x_column,
                      '좌표정보(Y)': y_column}

logging.basicConfig(
    format='%(asctime)s:%(levelname)s:%(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.INFO)


def create_csv_files(df: pd.DataFrame, path: str) -> None:
    have_essential_data = dataframe_separator.have_essential_data(df, x_column, y_column, address)
    csv_writer.save_csv(df[have_essential_data], path, '필수값O')
    csv_writer.save_csv(df[~have_essential_data], path, '필수값X')


if __name__ == "__main__":
    df: pd.DataFrame

    # read csv file
    logging.info("Read .csv file")
    df = csv_reader.read_dataframe("data/data.csv", encoding='utf-8')

    # preprocessing
    logging.info("Preprocessing pandas dataframe")
    df = subset_manager.make_subset(df, column_list)

    logging.info("날짜 변경하기")
    df = date_transformer.transform_date(df, '데이터갱신일자')

    logging.info('Rename column')
    df = subset_manager.rename_column(df, rename_column_dict)

    logging.info('transform coordinate system')
    df = coordinate_translator.transform_coordinate_system(df, x_column, y_column, 'EPSG:5174', 'EPSG:4326')

    # replace coordinate inf to nan
    df = df.replace(np.inf, np.nan)

    logging.info('separate data frame')

    # 영업중
    opened_df = dataframe_separator.open_hospital(df)
    logging.info('영업중인 병원 .csv 저장')
    create_csv_files(opened_df, "영업중")

    # 휴업중
    suspended_df = dataframe_separator.suspended_hospital(df)
    logging.info('휴업중인 병원 .csv 저장')
    create_csv_files(suspended_df, "휴업중")

    # 폐업, 말소
    closed_df = dataframe_separator.closed_hospital(df)
    logging.info('폐업-말소된 병원 .csv 저장')
    create_csv_files(closed_df, "폐업-말소")
