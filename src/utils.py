import json


def get_transit_info(path: str) -> list[dict[str, str | int]]:
    """ Получение данных о финансовых транзакциях """
    try:
        with open(path, encoding='utf-8') as operations_file:
            try:
                transit_info = json.load(operations_file)
            except json.JSONDecodeError:
                print('Ошибка декодирования файла')
                return []
    except FileNotFoundError:
        print('Файл не найден')
        return []

    return transit_info


if __name__ == '__main__':  # pragma: no cover
    print(get_transit_info(r'..\data\operations.json'))
