from typing import Any, Iterable


def filter_by_currency(transactions: list[dict[Any]], currency: str) -> Iterable:
    """ Возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной """
    for transaction in transactions:
        if not transaction['operationAmount']['currency']['name']:
            raise KeyError('Информация по транзакциям отсутствует')

    if not transactions:
        raise ValueError('Информация отсутствует')

    return (item for item in transactions if item['operationAmount']['currency']['name'] == currency)


def transaction_descriptions(transactions: list[dict[Any]]) -> Iterable:
    """ Возвращает описание каждой операции по очереди """
    for transaction in transactions:
        if not transaction:
            raise StopIteration('Информация отсутствует')
        else:
            description = transaction.get('description')
            yield description


def card_number_generator(start: int, stop: int) -> Iterable:
    """
    Генератор, который выдает номера банковских карт
    в формате XXXX XXXX XXXX XXXX,
    где X — цифра номера карты
    """
    if stop < start:
        raise ValueError('Ошибка. Неверные данные')

    if start < 0 or stop < 0:
        raise ValueError('Ошибка. Отрицательные значения')

    for i in range(start, stop + 1):
        count_0 = '0' * (16 - len(str(i)))
        number_card = count_0 + str(i)
        yield f'{number_card[:4]} {number_card[4:8]} {number_card[8:12]} {number_card[12:]}'
