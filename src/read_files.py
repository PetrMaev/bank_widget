from typing import Any

import pandas as pd
import csv


def read_csv(path_file: str) -> list[dict[str | Any, str | Any]]:
    """ Считывает данные из csv-файла """
    result = []
    with open(path_file, encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';')
        for row in reader:
            result.append(row)
    return result


def read_excel(path_file: str) -> list[dict[str, str | Any]]:
    """ Считывает данные из excel-файла """
    excel_data = pd.read_excel(path_file).to_dict(orient='records')
    return excel_data


if __name__ == '__main__':  # pragma: no cover
    # print(read_csv('../data/transactions.csv'))
    print(read_excel('../data/transactions_excel.xlsx'))
