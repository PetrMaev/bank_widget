import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(my_transactions):
    usd_transactions = filter_by_currency(my_transactions, "USD")
    assert next(usd_transactions) == {'id': 939719570, 'state': 'EXECUTED',
                                      'date': '2018-06-30T02:08:58.425572',
                                      'operationAmount': {'amount': '9824.07',
                                                          'currency': {'name': 'USD', 'code': 'USD'}},
                                      'description': 'Перевод организации',
                                      'from': 'Счет 75106830613657916952',
                                      'to': 'Счет 11776614605963066702'}
    assert next(usd_transactions) == {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878',
                                      'operationAmount': {'amount': '79114.93',
                                                          'currency': {'name': 'USD', 'code': 'USD'}},
                                      'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542',
                                      'to': 'Счет 75651667383060284188'}
    assert next(usd_transactions) == {'id': 895315941, 'state': 'EXECUTED', 'date': '2018-08-19T04:27:37.904916',
                                      'operationAmount': {'amount': '56883.54',
                                                          'currency': {'name': 'USD', 'code': 'USD'}},
                                      'description': 'Перевод с карты на карту',
                                      'from': 'Visa Classic 6831982476737658',
                                      'to': 'Visa Platinum 8990922113665229'}
    with pytest.raises(StopIteration):
        next(usd_transactions)


def test_filter_by_currency_invalid_key(my_transactions_no_currency):
    with pytest.raises(KeyError):
        filter_by_currency(my_transactions_no_currency, "USD")


def test_filter_by_currency_invalid_data():
    with pytest.raises(ValueError):
        filter_by_currency([], "USD")


def test_transaction_descriptions(my_transactions):
    info = transaction_descriptions(my_transactions)
    assert next(info) == 'Перевод организации'
    assert next(info) == 'Перевод со счета на счет'
    assert next(info) == 'Перевод со счета на счет'
    assert next(info) == 'Перевод с карты на карту'
    assert next(info) == 'Перевод организации'
    with pytest.raises(StopIteration):
        next(info)


def test_transaction_descriptions_invalid_data():
    with pytest.raises(StopIteration):
        next(transaction_descriptions([]))


@pytest.mark.parametrize('start, stop, expected',
                         [
                             (1, 3, ['0000 0000 0000 0001', '0000 0000 0000 0002', '0000 0000 0000 0003']),
                             (4, 5, ['0000 0000 0000 0004', '0000 0000 0000 0005']),
                         ]
                         )
def test_card_number_generator(start, stop, expected):
    gen = card_number_generator(start, stop)
    assert list(gen) == expected



def test_card_number_generator_error():
    with pytest.raises(ValueError) as error:
        list(card_number_generator(3, 1))
    assert str(error.value) == 'Ошибка. Неверные данные'


def test_card_number_generator_error_2():
    with pytest.raises(ValueError) as error:
        list(card_number_generator(-1, 3))
    assert str(error.value) == 'Ошибка. Отрицательные значения'
