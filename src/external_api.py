import os
import logging
import requests
from dotenv import load_dotenv

from config import PATH_LOGS

api_logger = logging.getLogger("external_api")
file_handler = logging.FileHandler(os.path.join(PATH_LOGS, "external_api.log"))
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
api_logger.addHandler(file_handler)
api_logger.setLevel(logging.INFO)

def convert_amount_by_currency(cur_from: str, cur_to: str, amount: float) -> float:

    load_dotenv()
    api_key = os.getenv("API_KEY")

    url = f"https://api.apilayer.com/exchangerates_data/convert?to={cur_to}&from={cur_from}&amount={amount}"

    payload = {}
    headers = {"apikey": api_key}

    api_logger.info(f"Вызов метода GET по url = {url}")
    try:
        response = requests.request("GET", url, headers=headers, data=payload)
    except Exception as ex:
        api_logger.error(f"При выполнения запроса возникла ошибка: {ex}", exc_info=True)

    status_code = response.status_code
    result = response.json()


    if status_code == 200:
        return float(result["result"])
    else:
        api_logger.error(f"Ошибка запроса, статус-код: {status_code}, сообщение: {result}")
        raise requests.exceptions.RequestException(f"Ошибка запроса, статус-код: {status_code}, сообщение: {result}")


if __name__ == "__main__":
    print(convert_amount_by_currency("RUB", "USD", 100))
