"""Module contains reusable methods for reading excel, csv, json"""
import pandas


def get_sheet_into_list(excel_location, sheet_name):
    df = pandas.read_excel(io=excel_location, sheet_name=sheet_name)
    return df.values.tolist()


def get_csv_into_list(csv_location):
    df = pandas.read_csv(filepath_or_buffer=csv_location, delimiter=";")
    return df.values.tolist()


def get_json_as_dic(json_location):
    json_dic = pandas.read_json(path_or_buf=json_location, typ="dictionary")
    return json_dic