import json
import logging

logger = logging.getLogger()
file_handler = logging.FileHandler(r"../logs/utils.log", "w", encoding="utf-8")
logger.addHandler(file_handler)
file_formatter = logging.Formatter(
    "%(asctime)s; %(filename)s; %(levelname)s; %(message)s", "%d-%m-%Y %H:%M:%S"
)
file_handler.setFormatter(file_formatter)
logger.setLevel(logging.DEBUG)


def get_transit_info(path: str) -> list[dict[str, str | int]]:
    """Получение данных о финансовых транзакциях из JSON-файла"""
    if not path:
        logger.error("Ошибка. Данные отсутствуют")
        raise ValueError("Данные отсутствуют")
    if not isinstance(path, str):
        logger.error("Ошибка типа данных")
        raise TypeError("Ошибка типа данных")

    logger.info(f"Открытие JSON-файла по пути: {path}")
    try:
        with open(path, encoding="utf-8") as operations_file:
            transit_info = json.load(operations_file)
    except json.JSONDecodeError:
        logger.error("Ошибка декодирования файла")
        print("Ошибка декодирования файла")
        return []
    except FileNotFoundError:
        logger.error("Ошибка. Файл не найден")
        print("Файл не найден")
        return []

    return transit_info


if __name__ == "__main__":  # pragma: no cover
    print(get_transit_info(r"..\data\operations.json"))
    print(get_transit_info(r"..\operations.json"))
