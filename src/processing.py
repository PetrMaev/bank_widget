def filter_by_state(user_info: list, state: str = 'EXECUTED') -> list:
    """ Фильтрует список словарей по опциональному значению ключа state"""
    filtered_user_info = []
    for info in user_info:
        if info['state'] == state:
            filtered_user_info.append(info)
        else:
            continue
    return filtered_user_info


def sort_by_date(user_info: list, reversing: bool = True) -> list:
    """ Сортирует список словарей по дате по убыванию"""
    user_info.sort(key=lambda x: x['date'], reverse=reversing)
    return user_info


if __name__ == '__main__':
    print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                           {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                           {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                           {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))

    print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
