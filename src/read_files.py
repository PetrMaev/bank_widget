import pandas as pd
import csv


def read_csv(path_file: str) -> list[dict[str, str | int]]:
    """ Считывает данные из csv-файла """
    result = []
    with open(path_file, encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';')

        for row in reader:
            result.append(row)
    return result



if __name__ == '__main__':
    print(read_csv('../data/transactions.csv'))

