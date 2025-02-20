import logging
import os
import re

from config import PATH_LOGS

masks_logger = logging.getLogger("masks")
file_handler = logging.FileHandler(os.path.join(PATH_LOGS, "masks.log"))
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
masks_logger.addHandler(file_handler)
masks_logger.setLevel(logging.INFO)


def get_mask_card_number(card_number: str) -> str:
    """Функция get_mask_card_number
     принимает на вход номер карты и возвращает ее маску. Номер карты замаскирован и отображается в формате
    XXXX XX** **** XXXX
    """
    # проверка что передана строка
    if not isinstance(card_number, str):

        masks_logger.error(
            f"В процессе выполнения функции get_mask_card_number с параметром {card_number} произошла ошибка типа."
        )
        raise TypeError("Номер карты должен быть строкой")

    # проверка соответствия номера карты шаблону
    regex_card = re.compile(pattern=r"^([0-9]{4})\s?([0-9]{4})\s?([0-9]{4})\s?([0-9]{4})$")
    if not regex_card.match(card_number):
        masks_logger.error(
            f"В процессе выполнения функции get_mask_card_number с параметром {card_number} произошла ошибка значения."
        )
        raise ValueError("Номер карты не соответствует формату")

    card_number.replace(" ", "")
    result = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]

    masks_logger.info(f"Функция get_mask_card_number с параметром {card_number} вернула значение {result}")
    return result


def get_mask_account(account_number: str) -> str:
    """Функция
    get_mask_account
     принимает на вход номер счета и возвращает его маску. Номер счета замаскирован и отображается в формате
    **XXXX"""

    # проверка, что передана строка
    if not isinstance(account_number, str):
        masks_logger.error(
            f"В процессе выполнения функции get_mask_account с параметром {account_number} произошла ошибка типа."
        )
        raise TypeError("Номер счета должен быть строкой")

    # проверка, что номер счета соответствует формату
    regex_card = re.compile(pattern="^[0-9]{9,18}$")
    if not regex_card.match(account_number):
        masks_logger.error(
            f"В процессе выполнения функции get_mask_account с параметром {account_number} произошла ошибка значения."
        )
        raise ValueError("Номер счета не соответствует формату")

    result = "**" + account_number[-4:]
    masks_logger.info(f"Функция get_mask_account с параметром {account_number} вернула значение {result}")
    return result


if __name__ == "__main__":
    get_mask_account("123456789987654321")
