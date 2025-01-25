from typing import Generator

def filter_by_currency(transactions: list[dict], currency_code: str) -> Generator[dict, None, None]:
    """
    Функция принимает список транзакций и возвращает генератор,
    который поочередно возвращает транзакции с определенной валютой
    """
    generator = (transaction for transaction in transactions if transaction.get("operationAmount",{}).get("currency",{}).get("code") == currency_code)
    for transaction in generator:
        yield transaction


def transaction_descriptions(transactions: list[dict]) -> Generator[str, None, None]:
    """Функция принимает список транзакций и возвращает генератор, который поочередно возвращает описание транзакций"""
    descriptions = (transaction.get("description") for transaction in transactions)
    for description in descriptions:
        yield description


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    result_str = "0123 4567 8901 2345"
    nums = (format_card_number('{:0{length}}'.format(x, length=16)) for x in range(start, stop + 1))
    for num in nums:
        yield num


def format_card_number(input_str: str) -> str:
    """Преобразует строку вида "1234567812345678" в строку номера карты - "1234 5678 1234 5678" """
    return input_str[:4] + " " + input_str[4:8] + " " + input_str[8:12] + " " + input_str[12:]

