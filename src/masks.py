import logging

logger = logging.getLogger()
file_handler = logging.FileHandler(r"../logs/masks.log", "w", encoding="utf-8")
logger.addHandler(file_handler)
file_formatter = logging.Formatter(
    "%(asctime)s; %(filename)s; %(levelname)s; %(message)s", "%d-%m-%Y %H:%M:%S"
)
file_handler.setFormatter(file_formatter)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: int) -> str:
    """ Функция, которая принимает на вход номер карты и возвращает ее маску """
    logger.info(f'Начало работы функции возврата маски номера карты.')
    if not isinstance(card_number, int):
        logger.error('Ошибка. Неверный тип данных.')
        raise TypeError("Неверный тип данных")

    card_number_str = str(card_number)
    if len(card_number_str) < 16 or len(card_number_str) == 0:
        logger.error('Ошибка. Неверный формат данных.')
        raise ValueError("Неверный формат данных")
    else:
        logger.info('Успешный возврат маски номера карты.')
        return (
                card_number_str[:4] + " " + card_number_str[4:6] + "**" + " " + "****" + " " + card_number_str[12:]
        )


def get_mask_account(account_number: int) -> str:
    """ Функция, которая принимает на вход номер счета и возвращает его маску """
    logger.info(f'Начало работы функции возврата маски номера счета.')
    if not isinstance(account_number, int):
        logger.error('Ошибка. Неверный тип данных.')
        raise TypeError("Неверный тип данных")

    account_number_str = str(account_number)
    if len(account_number_str) < 16 or len(account_number_str) == 0:
        logger.error('Ошибка. Неверный формат данных.')
        raise ValueError("Неверный формат данных")
    mask_account_number = account_number_str.replace(account_number_str[:16], "**")
    logger.info('Успешный возврат маски номера счета.')
    return mask_account_number


if __name__ == "__main__":  # pragma: no cover
    print(get_mask_card_number(7000792289606361))
    print(get_mask_account(73654108430135874305))
    # print(get_mask_card_number([]))
    # print(get_mask_card_number(5436))
    print(get_mask_account(736))
