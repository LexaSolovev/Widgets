from typing import Generator

def filter_by_currency(transactions: list[dict], currency_code: str) -> Generator[dict]:
    """
    Функция принимает список транзакций и возвращает генератор,
    который поочередно возвращает транзакции с определенной валютой
    """

    generator = (transaction for transaction in transactions if transaction.get("operationAmount",{}).get("currency",{}).get("code") == currency_code)
    for transaction in generator:
        yield transaction


def transaction_descriptions(transactions):
    pass


def card_number_generator(start, stop):
    pass