from typing import Any

import pandas as pd


def read_csv(path_file: str) -> list[dict[str | Any, str | Any]]:
    """ Считывает данные из csv-файла """
    csv_data = pd.read_csv(path_file, delimiter=";").to_dict(orient="records")
    for elem in csv_data:
        elem.update({"id": int(elem["id"]), "amount": int(elem["amount"])})
        # Приведение всех данных фйлов к единому виду
        amount, currency_name, currency_code = (
            elem.pop("amount"),
            elem.pop("currency_name"),
            elem.pop("currency_code"),
        )
        elem.update(
            {
                "operationAmount": {
                    "amount": amount,
                    "currency": {"name": currency_name, "code": currency_code},
                }
            }
        )
    return csv_data


def read_excel(path_file: str) -> list[dict[str, str | Any]]:
    """ Считывает данные из excel-файла """
    excel_data = pd.read_excel(path_file).to_dict(orient="records")
    for elem in excel_data:
        elem.update({"id": int(elem["id"]), "amount": int(elem["amount"])})
        # Приведение всех данных фйлов к единому виду
        amount, currency_name, currency_code = (
            elem.pop("amount"),
            elem.pop("currency_name"),
            elem.pop("currency_code"),
        )
        elem.update(
            {
                "operationAmount": {
                    "amount": amount,
                    "currency": {"name": currency_name, "code": currency_code},
                }
            }
        )
    return excel_data


if __name__ == "__main__":  # pragma: no cover
    print(read_csv('../data/transactions.csv'))
    # print(read_excel("../data/transactions_excel.xlsx"))
