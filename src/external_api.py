import os

import requests
from dotenv import load_dotenv


def convert_amount_by_currency(cur_from: str, cur_to: str, amount: float) -> float:

    load_dotenv()
    api_key = os.getenv("API_KEY")

    url = f"https://api.apilayer.com/exchangerates_data/convert?to={cur_to}&from={cur_from}&amount={amount}"

    payload = {}
    headers = {"apikey": api_key}

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    result = response.json()

    if status_code == 200:
        return float(result["result"])
    else:
        raise requests.exceptions.RequestException(f"Ошибка запроса, статус-код: {status_code}, сообщение: {result}")


if __name__ == "__main__":
    print(convert_amount_by_currency("RUB", "USD", 100))
