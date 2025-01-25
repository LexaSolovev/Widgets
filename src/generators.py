def filter_by_currency(transactions: list[dict], currency_code: str):
    try:
        generator = (transaction for transaction in transactions if transaction.get("operationAmount").get("currency").get("code") == currency_code)
    except (AttributeError, StopIteration):
        return None
    else:
        for transaction in generator:
            yield transaction



def transaction_descriptions(transactions):
    pass


def card_number_generator(start, stop):
    pass