import config
from utils import read_utils


class DataSource:
    data_valid_login = [("admin", "pass", "OpenEMR"),
                        ("accountant", "accountant", "OpenEMR")]
    data_invalid_login = [("saul", "saul123", "Invalid username or password"),
                          ("kim", "kim123", "Invalid username or password")]

    # data_valid_login_excel=read_utils.get_sheet_into_list("../test_data/open_emr_data.xlsx","test_valid_login")
    # data_invalid_login_excel = read_utils.get_sheet_into_list("../test_data/open_emr_data.xlsx", "test_invalid_login")
    # data_valid_login_csv=read_utils.get_csv_into_list("../test_data/test_valid_login.csv")
    data_valid_login_excel = read_utils.get_sheet_into_list(config.test_data_path+r"\open_emr_data.xlsx", "test_valid_login")
    data_invalid_login_excel = read_utils.get_sheet_into_list(config.test_data_path+r"\open_emr_data.xlsx", "test_invalid_login")
    data_valid_login_csv = read_utils.get_csv_into_list(config.test_data_path+r"\test_valid_login.csv")