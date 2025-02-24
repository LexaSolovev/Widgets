import os.path

from config import PATH_DATA
from src.processing import filter_by_description, filter_by_state, sort_by_date
from src.utils import get_transactions_from_csv, get_transactions_from_excel, get_transactions_from_json
from src.widget import get_date, mask_account_card


def main():
    # Приветствие и выбор меню
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    menu = {
        "1": "1. Получить информацию о транзакциях из JSON-файла",
        "2": "2. Получить информацию о транзакциях из CSV-файла",
        "3": "3. Получить информацию о транзакциях из XLSX-файла",
    }
    str_menu = "\n".join(menu.values())
    while True:
        print("Выберите необходимый пункт меню:")
        print(str_menu)
        ui_menu = input()
        if ui_menu not in menu.keys():
            print(f"Неверный ввод! Ожидаются цифры {list(menu.keys())}!")
            continue
        else:
            break
    print(f"Выбор сделан: {menu[ui_menu]}")

    transactions = []
    if ui_menu == "1":
        path = os.path.join(PATH_DATA, "operations.json")
        transactions = get_transactions_from_json(path)
    elif ui_menu == "2":
        path = os.path.join(PATH_DATA, "transactions.csv")
        transactions = get_transactions_from_csv(path)
    elif ui_menu == "3":
        path = os.path.join(PATH_DATA, "transactions_excel.xlsx")
        transactions = get_transactions_from_excel(path)

    # Выбор режима фильтрации
    while True:
        print(
            """
        Введите статус, по которому необходимо выполнить фильтрацию.
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
        """
        )
        ui_filter = input().upper()
        if ui_filter == "EXECUTED":
            print('Операции отфильтрованы по статусу "EXECUTED"')
            break
        elif ui_filter == "CANCELED":
            print('Операции отфильтрованы по статусу "CANCELED"')
            break
        elif ui_filter == "PENDING":
            print('Операции отфильтрованы по статусу "PENDING"')
            break
        else:
            print(f"Статус операции {ui_filter} не определен")

    transactions = filter_by_state(transactions, state=ui_filter)

    # Выбор опции сортировки по дате
    while True:
        print("""Отсортировать операции по дате? Да/Нет""")
        ui_sort_by_date = input().lower()
        if ui_sort_by_date == "да":
            is_sort_by_date = True
            break
        elif ui_sort_by_date == "нет":
            is_sort_by_date = False
            break
        else:
            print("Некорректный ввод!")

    # Выбор опции сортировки reverse_option = True - по-возрастанию, False - по-убыванию
    if is_sort_by_date:
        while True:
            print("Отсортировать по возрастанию(1) или по убыванию(2)?")
            ui_reverse = input()
            if ui_reverse == "1":
                reverse_option = True
                break
            elif ui_reverse == "2":
                reverse_option = False
                break
            else:
                print("Некорректный ввод!")
        transactions = sort_by_date(transactions, reverse_option=reverse_option)

    # Выбор опции вывода только рублевых транзакций is_only_rub = True/False
    is_only_rub = False
    while True:
        print("Выводить только рублевые транзакции? Да/Нет")
        ui_only_rub = input().lower()
        if ui_only_rub == "да":
            is_only_rub = True
            break
        elif ui_only_rub == "нет":
            break
        else:
            print("Некорректный ввод!")

    # Выбор режима фильтрации по описанию filter_description
    filter_description = ""
    while True:
        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        ui_filter_description = input().lower()
        if ui_filter_description == "да":
            filter_description = input("Введите текст для фильтрации:")
            break
        elif ui_filter_description == "нет":
            break
        else:
            print("Некорректный ввод!")

    if filter_description:
        transactions = filter_by_description(transactions, search_str=filter_description)

    # Вывод итогового списка транзакций
    if not len(transactions):
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    for transaction in transactions:
        if ui_menu == "1":
            transaction_currency_name = transaction.get("operationAmount", {}).get("currency", {}).get("name", "")
            transaction_currency_code = transaction.get("operationAmount", {}).get("currency", {}).get("code", "")
            transaction_sum = transaction.get("operationAmount", {}).get("amount", "")
        elif ui_menu in ("2", "3"):
            transaction_currency_name = transaction.get("currency_name", "")
            transaction_currency_code = transaction.get("currency_code", "")
            transaction_sum = transaction.get("amount", "")

        if not is_only_rub or transaction_currency_code == "RUB":

            output_date = get_date(transaction.get("date", ""))
            output_description = transaction.get("description", "")

            print(f"{output_date} {output_description}")

            transaction_from = transaction.get("from", "")
            transaction_to = transaction.get("to", "")
            transaction_to = mask_account_card(transaction_to)
            if transaction_from:
                transaction_from = mask_account_card(transaction_from)
                output_from_to = f"{transaction_from} -> {transaction_to}"
            else:
                output_from_to = f"{transaction_to}"

            print(output_from_to)

            output_sum = f"Сумма: {transaction_sum} {transaction_currency_name}"

            print(output_sum)


if __name__ == "__main__":
    main()
    # data = [
    #     {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    #     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    #     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    #     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    # ]
    # print(get_mask_card_number("1234567812345678"))
    # print(get_mask_account("1234123412356567"))
    # print(filter_by_state(data, state="CANCELED"))
    # print(sort_by_date(data))
