def get_mask_card_number(card_number: str) -> str:
    """Функция get_mask_card_number
     принимает на вход номер карты и возвращает ее маску. Номер карты замаскирован и отображается в формате
    XXXX XX** **** XXXX
    """
    return card_number[:4] + " " + card_number[5:7] + "** **** " + card_number[-4:]


def get_mask_account(account_number: str) -> str:
    """Функция
    get_mask_account
     принимает на вход номер счета и возвращает его маску. Номер счета замаскирован и отображается в формате
    **XXXX"""
    return "**" + account_number[-4:]
