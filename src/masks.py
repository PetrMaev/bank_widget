def get_mask_card_number(card_number: int) -> str:
    """ Функиця, которая принимает на вход номер карты и возвращает ее маску"""
    if not isinstance(card_number, int):
        raise TypeError("Неверный тип данных")

    card_number_str = str(card_number)
    if len(card_number_str) < 16 or len(card_number_str) == 0:
        raise ValueError("Неверный формат данных")
    else:
        return (card_number_str[:4] + " " + card_number_str[4:6] + "**" + " " + "****" + " " + card_number_str[12:])


def get_mask_account(account_number: int) -> str:
    """ Функция которая принимает на вход номер счета и возвращает его маску"""
    if not isinstance(account_number, int):
        raise TypeError("Неверный тип данных")

    account_number_str = str(account_number)
    if len(account_number_str) < 16 or len(account_number_str) == 0:
        raise ValueError("Неверный формат данных")
    mask_account_number = account_number_str.replace(account_number_str[:16], "**")
    return mask_account_number


if __name__ == '__main__':          # pragma: no cover
    print(get_mask_card_number(7000792289606361))
    print(get_mask_account(73654108430135874305))
    # print(get_mask_card_number([]))
    # print(get_mask_account(736))
