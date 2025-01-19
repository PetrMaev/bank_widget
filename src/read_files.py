from typing import Any

import pandas as pd


def read_csv(path_file: str) -> list[dict[str | Any, str | Any]]:
    """ Считывает данные из csv-файла """
    csv_data = pd.read_csv(path_file, delimiter=';').to_dict(orient='records')
    return csv_data


def read_excel(path_file: str) -> list[dict[str, str | Any]]:
    """ Считывает данные из excel-файла """
    excel_data = pd.read_excel(path_file).to_dict(orient='records')
    return excel_data


if __name__ == '__main__':  # pragma: no cover
    # print(read_csv('../data/transactions.csv'))
    print(read_excel('../data/transactions_excel.xlsx'))
