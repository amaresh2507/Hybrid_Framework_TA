from utils import read_utils
class DataSource:
    data_valid_login = [('admin', 'pass', 'OpenEMR'), ('accountant', 'accountant', 'OpenEMR')]
    data_invalid_login = [('saul', 'saul123', 'Invalid'), ('john', 'john123', 'Invalid')]

    data_valid_login_excel = read_utils.get_sheet_into_list("../test_data/open_emr_data.xlsx","valid_login")
    data_invalid_login_excel = read_utils.get_sheet_into_list("../test_data/open_emr_data.xlsx", "invalid_login")

    data_valid_login_csv = read_utils.get_csv_into_list("../test_data/open_emr_csv.csv")

    print(data_valid_login_csv)