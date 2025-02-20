import json
import logging
import os
import csv
import pandas as pd

from config import PATH_DATA, PATH_LOGS
from src.external_api import convert_amount_by_currency

utils_logger = logging.getLogger("utils")
file_handler = logging.FileHandler(os.path.join(PATH_LOGS, "utils.log"))
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
utils_logger.addHandler(file_handler)
utils_logger.setLevel(logging.INFO)


def get_transactions_from_json(path_to_json: str) -> list[dict]:
    """Функция принимает путь до JSON файла и возвращает данные о транзакциях в виде списка словарей"""
    utils_logger.info(f"Запись транзакций в файл {path_to_json}")
    try:
        with open(path_to_json) as json_file:
            json_obj = json.load(json_file)
    except Exception as ex:
        utils_logger.error(f"При выполнении функции get_transactions_from_json произошла ошибка: {ex}")

    return json_obj


def get_amount(transaction: dict, currency: str = "RUB") -> float:
    """Функция возвращает сумму транзакции в нужной валюте currency: "RUB" или "USD" или "EUR" """

    utils_logger.info("Начало выполнения функции get_amount")

    transaction_currency = transaction.get("operationAmount", {}).get("currency", {}).get("code", "")
    transaction_amount = float(transaction.get("operationAmount", {}).get("amount", 0))

    if transaction_currency == currency:
        utils_logger.info(
            f"Конвертации валюты не требуется, возвращается сумма транзакции: {transaction_amount} {currency}"
        )
        return transaction_amount
    else:
        utils_logger.info(f"Требуется конвертация валюты из {transaction_currency} в {currency}")
        return convert_amount_by_currency(transaction_currency, currency, transaction_amount)


def get_transactions_from_csv(path_to_csv: str) -> list[dict]:
    """Функция принимает путь до CSV файла и возвращает данные о транзакциях в виде списка словарей"""

    with open(path_to_csv) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';')
        return list(reader)


def get_transactions_from_excel(path_to_excel: str) -> list[dict]:
    """Функция принимает путь до EXCEL файла и возвращает данные о транзакциях в виде списка словарей"""

    transactions_df = pd.read_excel(path_to_excel, )
    return json.loads(transactions_df.to_json(orient='records', force_ascii='list[dict]'))


if __name__ == "__main__":
    # path_to_json = os.path.join(PATH_DATA, "operations.json")
    # transactions = get_transactions_from_json(path_to_json)
    # print(get_amount(transactions[1]))
    # path_to_csv = os.path.join(PATH_DATA, "transactions.csv")
    # print(get_transactions_from_csv(path_to_csv)[0:4])
    path_to_excel = os.path.join(PATH_DATA, "transactions_excel.xlsx")
    print(get_transactions_from_excel(path_to_excel)[0:4])
