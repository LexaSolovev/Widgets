def filter_by_currency(transactions: list[dict], currency_code: str):
    generator = (transaction for transaction in transactions if transaction.get("operationAmount").get("currency").get("code") == currency_code)
    for transaction in generator:
        yield dict(transaction)



def transaction_descriptions(transactions):
    pass


def card_number_generator(start, stop):
    pass