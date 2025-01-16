import re


def get_mask_card_number(card_number: str) -> str:
    """Функция get_mask_card_number
     принимает на вход номер карты и возвращает ее маску. Номер карты замаскирован и отображается в формате
    XXXX XX** **** XXXX
    """
    #проверка что передана строка
    if not isinstance(card_number, str):
        raise TypeError("Номер карты должен быть строкой")

    #проверка соответствия номера карты шаблону
    regex_card = re.compile(pattern="^([0-9]{4}) ([0-9]{4}) ([0-9]{4}) ([0-9]{4})$")
    if not regex_card.match(card_number):
        raise ValueError("Номер карты не соответствует формату")

    return card_number[:4] + " " + card_number[5:7] + "** **** " + card_number[-4:]


def get_mask_account(account_number: str) -> str:
    """Функция
    get_mask_account
     принимает на вход номер счета и возвращает его маску. Номер счета замаскирован и отображается в формате
    **XXXX"""

    # проверка, что передана строка
    if not isinstance(account_number, str):
        raise TypeError("Номер счета должен быть строкой")

    # проверка, что номер счета соответствует формату
    regex_card = re.compile(pattern="^[0-9]{9,18}$")
    if not regex_card.match(account_number):
        raise ValueError("Номер счета не соответствует формату")

    return "**" + account_number[-4:]
