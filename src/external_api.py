import os
import requests
from dotenv import load_dotenv
from typing import Any

load_dotenv()


def get_sum_transit(transaction: dict[str, Any]) -> float | str:
    """ Получение суммы транзакции в рублях """
    payload = {}
    get_api = os.getenv('API_KEY')
    headers = {"apikey": f"{get_api}"}
    if not transaction:
        raise ValueError('Информация о транзакциях отсутствует')

    if not isinstance(transaction, dict | list):
        raise TypeError('Неверные исходные данные')

    if not transaction['operationAmount']:
        raise KeyError('Информация отсутствует')

    try:
        if transaction['operationAmount']['currency']['code'] == 'USD':
            amount_usd = transaction['operationAmount']['amount']
            url = f'https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount={amount_usd}'
            response = requests.get(url, headers=headers, data=payload)
            response.raise_for_status()
            return response.json()['result']
        elif transaction['operationAmount']['currency']['code'] == 'EUR':
            amount_eur = transaction['operationAmount']['amount']
            url = f'https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount={amount_eur}'
            response = requests.get(url, headers=headers, data=payload)
            response.raise_for_status()
            return response.json()['result']
        elif transaction['operationAmount']['currency']['code'] == 'RUB':
            return float(transaction['operationAmount']['amount'])
    except requests.exceptions.RequestException:
        return 'An error occurred. Please try again later.'


if __name__ == '__main__':  # pragma: no cover
    transaction_rub = {'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
                       'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                       'description': 'Перевод организации', 'from': 'Maestro 1596837868705199',
                       'to': 'Счет 64686473678894779589'}
    transaction_usd = {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364',
                       'operationAmount': {'amount': '8220.37', 'currency': {'name': 'USD', 'code': 'USD'}},
                       'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758',
                       'to': 'Счет 35383033474447895560'}
    transaction_eur = {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364',
                       'operationAmount': {'amount': '1100', 'currency': {'name': 'EUR', 'code': 'EUR'}},
                       'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758',
                       'to': 'Счет 35383033474447895560'}

    print(get_sum_transit(transaction_rub))
    print(get_sum_transit(transaction_usd))
    print(get_sum_transit(transaction_eur))
