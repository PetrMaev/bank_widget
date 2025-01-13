from typing import Any


def filter_by_state(
    user_info: list[dict[str, Any]], state: str = "EXECUTED"
) -> list[dict[str, Any]]:
    """Фильтрует список словарей по опциональному значению ключа state"""
    if not user_info:
        raise ValueError("Неверный формат данных")

    filtered_user_info = []
    for info in user_info:
        if info.get("state") == state:
            filtered_user_info.append(info)
        else:
            continue
    return filtered_user_info


def sort_by_date(
    user_info: list[dict[str, Any]], reversing: bool = True
) -> list[dict[str, Any]]:
    """Сортирует список словарей по дате по убыванию"""
    if not user_info:
        raise ValueError("Неверный формат данных")

    for info in user_info:
        if info.get("date"):
            user_info.sort(key=lambda x: x["date"], reverse=reversing)
        else:
            continue

    return user_info


if __name__ == "__main__":  # pragma: no cover
    print(
        filter_by_state(
            [
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                },
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                },
                {
                    "id": 615064591,
                    "state": "CANCELED",
                    "date": "2018-10-14T08:21:33.419441",
                },
            ]
        )
    )

    print(
        sort_by_date(
            [
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                },
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                },
                {
                    "id": 615064591,
                    "state": "CANCELED",
                    "date": "2018-10-14T08:21:33.419441",
                },
            ]
        )
    )
