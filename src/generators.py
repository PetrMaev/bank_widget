def filter_by_currency(transactions: list[dict], currency: str) -> iter:
    """ Возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной """
    return (item for item in transactions if item['operationAmount']['currency']['name'] == currency)


def transaction_descriptions(transactions: list[dict]) -> iter:
    """ Возвращает описание каждой операции по очереди """
    for transaction in transactions:
        description = transaction.get('description')
        yield description
