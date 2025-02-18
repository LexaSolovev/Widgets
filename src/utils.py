import json
import os
from config import PATH_DATA


def get_transactions_from_json(path_to_json:str) -> list[dict]:
    """Функция принимает путь до JSON файла и возвращает данные о транзакциях в виде списка словарей"""

    with open(path_to_json) as json_file:
        json_obj = json.load(json_file)

    return json_obj


if __name__ == "__main__":
    operations_path = os.path.join(PATH_DATA, "operations.json")
    print(get_transactions_from_json(operations_path))