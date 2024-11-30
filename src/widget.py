from masks import get_mask_card_number
from masks import get_mask_account

def mask_account_card(account_card: str) -> str:
    """ Функция, которая обрабатывает информацию о картах"""
    name_account = ''
    number = ''
    for sym in account_card:
        if sym.isalpha() or sym == ' ':
            name_account += sym
        elif sym.isdigit():
            number += sym
    if len(number) == 16:
        mask = get_mask_card_number(number)
    elif len(number) == 20:
        mask = get_mask_account(number)
    return (name_account + ' ' + mask)

if __name__ == '__main__':
    print(mask_account_card('Visa Platinum 7000792289606361'))
    print(mask_account_card('Счет 73654108430135874305'))
