import json
import os
from config import PATH_DATA
from external_api import convert_amount_by_currency

def get_transactions_from_json(path_to_json:str) -> list[dict]:
    """Функция принимает путь до JSON файла и возвращает данные о транзакциях в виде списка словарей"""

    with open(path_to_json) as json_file:
        json_obj = json.load(json_file)

    return json_obj


def get_amount(transaction:dict, currency:str="RUB") -> float:
    """Функция возвращает сумму транзакции в нужной валюте currency: "RUB" или "USD" или "EUR" """

    transaction_currency = transaction.get("operationAmount",{}).get("currency",{}).get("code","")
    transaction_amount = float(transaction.get("operationAmount",{}).get("amount",0))

    if transaction_currency == currency:
        return transaction_amount
    else:
        return convert_amount_by_currency(transaction_currency, currency, transaction_amount)


if __name__ == "__main__":
    operations_path = os.path.join(PATH_DATA, "operations.json")
    print(get_transactions_from_json(operations_path))