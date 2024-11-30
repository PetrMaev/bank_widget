def get_mask_card_number(card_number: int) -> str:
    """ Функиця, которая принимает на вход номер карты и возвращает ее маску"""
    card_number_str = str(card_number)
    return (card_number_str[:4] + " " + card_number_str[4:6] + "**" + " " + "****" + " " + card_number_str[12:])


def get_mask_account(account_number: int) -> str:
    """ Функция которая принимает на вход номер счета и возвращает его маску"""
    account_number_str = str(account_number)
    mask_account_number = account_number_str.replace(account_number_str[:16], "**")
    return mask_account_number
