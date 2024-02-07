'''Module uses reusable methods for reading excel, csvs, json'''
import pandas


def get_sheet_into_list(excel_location, sheet_name):
    df = pandas.read_excel(io=excel_location,sheet_name=sheet_name)
    return df.values.tolist()

def get_csv_into_list(csv_location):
    df = pandas.read_csv(filepath_or_buffer=csv_location,delimiter=";")
    return df.values.tolist()