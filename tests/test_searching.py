import pytest

from src.searching import get_transaction_info, get_number_of_transactions


def test_get_transaction_info(transactions):
    assert get_transaction_info(transactions, 'карт') == [
        {'id': 3598919, 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': 29740, 'currency_name': 'Peso',
         'currency_code': 'COP', 'from': 'Discover 3172601889670065', 'to': 'Discover 0720428384694643',
         'description': 'Перевод с карты на карту'}]


def test_get_number_of_transactions(transactions):
    assert get_number_of_transactions(transactions, ['Перевод организации', 'Перевод с карты на карту']) == {
        'Перевод организации': 1, 'Перевод с карты на карту': 1}
