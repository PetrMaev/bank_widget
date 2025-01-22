import re
from collections import Counter


def get_transaction_info(transit_info: list[dict], search_str: str) -> list[dict]:
    """
    Функция принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка.
    """
    result = []
    for transit in transit_info:
        if re.search(f'.*{search_str}.*', transit['description'], flags=re.IGNORECASE):
            result.append(transit)
    return result


def get_number_of_transactions(transit_info: list[dict], transit_categories: list) -> dict:
    """
    Функция принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории.
    """
    descriptions = []
    for category in transit_categories:
        for transit in transit_info:
            if category == transit.get('description'):
                descriptions.append(transit.get('description'))
    number_of_transactions = Counter(descriptions)
    return dict(number_of_transactions)


if __name__ == '__main__':  # pragma: no cover
    print(get_transaction_info([{'id': 650703, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 16210,
                                 'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391',
                                 'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'},
                                {'id': 3598919, 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': 29740,
                                 'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Discover 3172601889670065',
                                 'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'},
                                ], 'карт'))

    print(
        get_number_of_transactions([{'id': 650703, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 16210,
                                     'currency_name': 'Sol', 'currency_code': 'PEN',
                                     'from': 'Счет 58803664561298323391',
                                     'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'},
                                    {'id': 3598919, 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z',
                                     'amount': 29740,
                                     'currency_name': 'Peso', 'currency_code': 'COP',
                                     'from': 'Discover 3172601889670065',
                                     'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'},
                                    ], ['Перевод организации', 'Перевод с карты на карту']))
