from numpy import nan

from src.external_api import get_sum_transit
from src.processing import filter_by_state, sort_by_date
from src.read_files import read_csv, read_excel
from src.searching import get_transaction_info
from src.utils import read_json
from src.widget import get_date, mask_account_card


def main():
    """ Основная логика проекта. Связывает функциональности виджета банка между собой """
    # Приветствие
    print('Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n')

    # Выбор файла для обработки операций
    while True:
        question_1 = input('Выберите необходимый пункт меню: \n'
                           '1. Получить информацию о транзакциях из JSON-файла\n'
                           '2. Получить информацию о транзакциях из CSV-файла\n'
                           '3. Получить информацию о транзакциях из XLSX-файла\n'
                           'Место ввода данных: ')
        if question_1 == '1':
            print('Для обработки выбран JSON-файл')
            selected_file = read_json(r'.\data\operations.json')
            break
        elif question_1 == '2':
            print('Для обработки выбран CSV-файл')
            selected_file = read_csv('./data/transactions.csv')
            break
        elif question_1 == '3':
            print('Для обработки выбран XLSX-файл')
            selected_file = read_excel('./data/transactions_excel.xlsx')
            break
        else:
            print('Файл не выбран. Повторите попытку.\n')

    # Выбор статуса для фильтрации файла
    question_2 = input(
        'Введите статус, по которому необходимо выполнить фильтрацию.\n'
        'Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING: ')
    if question_2.upper() == 'EXECUTED' or question_2.upper() == 'CANCELED' or question_2.upper() == 'PENDING':
        filtered_file = filter_by_state(selected_file, question_2.upper())
        print(f'Операции отфильтрованы по статусу "{question_2.upper()}"')
    else:
        filtered_file = selected_file
        print(f'Статус операции "{question_2}" недоступен')

    # Выбор фильтрации по дате
    question_3 = input('Отсортировать операции по дате? Да/Нет ')
    if question_3.lower() == 'да':
        # Выбор фильтрации по возрастанию или по убыванию
        question_4 = input('Отсортировать по возрастанию или по убыванию? ')
        if question_4.lower() == 'по возрастанию':
            filtered_file_2 = sort_by_date(filtered_file, reversing=False)
        elif question_4.lower() == 'по убыванию':
            filtered_file_2 = sort_by_date(filtered_file)
        else:
            filtered_file_2 = filtered_file
            print(f'Фильтрация по "{question_4}" недоступна')
    elif question_3.lower() == 'нет':
        filtered_file_2 = filtered_file
    else:
        filtered_file_2 = filtered_file
        print(f'Фильтрация по "{question_3}" недоступна')

    # Выбор фильтрации по валюте
    question_5 = input('Выводить только рублевые транзакции? Да/Нет ')
    if question_5.lower() == 'да':
        # Выбор фильтрации по описанию
        question_6 = input('Отфильтровать список транзакций по определенному слову в описании? Да/Нет ')
        if question_6.lower() == 'да':
            search_string = input('Введите ключевое слово: ')
            result = get_transaction_info(filtered_file_2, search_string)
        elif question_6.lower() == 'нет':
            result = filtered_file_2
        else:
            result = filtered_file_2
            print(f'Фильтрация по {question_6} недоступна\n')

        # Вывод результата работы программы
        print('Распечатываю итоговый список транзакций...\n')

        print(f'Всего банковских операций в выборке: {len(result)}\n')

        for item in result:
            first_string = get_date(item['date']) + '  ' + item['description']
            print(first_string)
            if 'to' in item and 'from' in item:
                if item.get('from') is nan:
                    second_string = mask_account_card(item.get('to'))
                    print(second_string)
                else:
                    second_string = f'{mask_account_card(item.get('from'))}  ->  {mask_account_card(item.get('to'))}'
                    print(second_string)
            else:
                second_string = mask_account_card(item.get('to'))
                print(second_string)
            third_string = get_sum_transit(item)
            print(f'Сумма: {third_string} руб.\n')
    elif question_5.lower() == 'нет':
        # Выбор фильтрации по описанию
        question_6 = input('Отфильтровать список транзакций по определенному слову в описании? Да/Нет ')
        if question_6.lower() == 'да':
            search_string = input('Введите ключевое слово: ')
            result = get_transaction_info(filtered_file_2, search_string)
        elif question_6.lower() == 'нет':
            result = filtered_file_2
        else:
            result = filtered_file_2
            print(f'Фильтрация по {question_6} недоступна')

        # Вывод результата работы программы
        print('Распечатываю итоговый список транзакций...\n')

        print(f'Всего банковских операций в выборке: {len(result)}\n')

        for item in result:
            first_string = get_date(item['date']) + '  ' + item['description']
            print(first_string)
            if 'to' in item and 'from' in item:
                if item.get('from') is nan:
                    second_string = mask_account_card(item.get('to'))
                    print(second_string)
                else:
                    second_string = f'{mask_account_card(item.get('from'))}  ->  {mask_account_card(item.get('to'))}'
                    print(second_string)
            else:
                second_string = mask_account_card(item.get('to'))
                print(second_string)
            third_string = f'{item['operationAmount']['amount']} {item['operationAmount']['currency']['code']}'
            print(f'Сумма: {third_string}\n')

    else:
        return print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')


if __name__ == '__main__':
    main()
