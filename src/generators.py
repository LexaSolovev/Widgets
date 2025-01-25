def filter_by_currency(transactions: list[dict], currency_code: str):
    #Проверяем что тип входных данных соответсвует ожиданиям и список транзакций не пустой
    generator = (transaction for transaction in transactions if transaction.get("operationAmount",{}).get("currency",{}).get("code") == currency_code)
    for transaction in generator:
        yield transaction


def transaction_descriptions(transactions):
    pass


def card_number_generator(start, stop):
    pass