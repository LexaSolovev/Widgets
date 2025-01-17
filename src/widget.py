import re
from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """
    Функция принимает строку с названием карты/счета и номером карты/счета.
    Возвращает строку с зашифрованными номерами

    # Пример для карты
    Visa Platinum 7000792289606361  # входной аргумент
    Visa Platinum 7000 79** **** 6361  # выход функции
    # Пример для счета
    Счет 73654108430135874305  # входной аргумент
    Счет **4305  # выход функции
    """
    patern_card = re.compile(pattern="^[^0-9]+([0-9]{4}) ?([0-9]{4}) ?([0-9]{4}) ?([0-9]{4})$")
    if patern_card.match(data):
        pay_system = ""
        for s in data:
            if s.isdigit():
                break
            else:
                pay_system += s
        card_number = data.replace(" ", "")[-16:]
        mask_card_number = get_mask_card_number(card_number)
        return pay_system + mask_card_number
    else:
        data_list = data.split()
        data_list[-1] = get_mask_account(data_list[-1])
    return " ".join(data_list)


def get_date(date: str) -> str:
    """
    Функция принимает строку даты в формате "2024-03-11T02:26:18.671407"
    Возвращает строку даты в формате "ДД.ММ.ГГГГ"
    """
    return date[8:10] + "." + date[5:7] + "." + date[:4]


if __name__ == "__main__":
    print(mask_account_card("Visa Classic 6831982476737658"))
    print(get_date("2024-03-11T02:26:18.671407"))
