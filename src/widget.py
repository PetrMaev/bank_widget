from src.masks import get_mask_card_number
from src.masks import get_mask_account


def mask_account_card(account_card: str) -> str:
    """ Функция, которая обрабатывает информацию о картах и маскирует номер карты или счета"""
    name_account = ''
    number = ''
    mask = ''

    if not isinstance(account_card, str):
        raise TypeError("Неверный тип данных")

    for sym in account_card:
        if sym.isalpha() or sym == ' ':
            name_account += sym
        elif sym.isdigit():
            number += sym

    if len(number) == 0 or len(number) < 16:
        raise ValueError("Неверный формат данных")

    if len(number) == 16:
        mask = get_mask_card_number(int(number))
    elif len(number) == 20 or name_account == 'Счет ':
        mask = get_mask_account(int(number))

    return name_account + mask


def get_date(date: str) -> str:
    """
    Функция, которая принимает на вход данные в формате "2024-03-11T02:26:18.671407"
    и возвращает дату в формате ДД.ММ.ГГГГ
    """
    if len(date) == 0 or len(date) < 26 or 'T' not in date:
        raise ValueError("Неверный формат данных")

    new_date = date.split('T')[0].split('-')
    return '.'.join(reversed(new_date))


# if __name__ == '__main__':
#     print(mask_account_card('Visa Platinum 7000792289606361'))
#     print(mask_account_card('Счет 73654108430135874305'))
#     print(get_date('2024-03-11T02:26:18.671407'))
