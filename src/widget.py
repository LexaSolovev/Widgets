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
    if not isinstance(data, str):
        raise TypeError("Параметр data должен быть строкой")
    patern_card = re.compile(pattern="^[^0-9, ]+ ([0-9]{4}) ?([0-9]{4}) ?([0-9]{4}) ?([0-9]{4})$")
    patern_account = re.compile(pattern="^Счет [0-9]{9,18}$")
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
    elif patern_account.match(data):
        data_list = data.split()
        data_list[-1] = get_mask_account(data_list[-1])
        return " ".join(data_list)
    else:
        raise ValueError("Неверный формат данных")


def get_date(date: str) -> str:
    """
    Функция принимает строку даты в формате "2024-03-11T02:26:18.671407"
    Возвращает строку даты в формате "ДД.ММ.ГГГГ"
    """
    if not isinstance(date, str):
        raise TypeError

    return date[8:10] + "." + date[5:7] + "." + date[:4]


def is_valid_datetime(date_str: str) -> bool:
    """Проверка формата даты 'YYYY-MM-DDTHH:MM:SS.mmmmmm' """

    # Регулярное выражение для проверки строки с датой и временем
    pattern_date = """^(?P<year>\d{4})-(?P<month>0[1-9]|1[012])-(?P<day>0[1-9]|[12][0-9]|3[01])
    T(?P<hour>[01][0-9]|2[0-3]):(?P<minute>[0-5][0-9]):(?P<second>[0-5][0-9])\.(?P<microseconds>\d{6})$"""
    match = re.match(pattern_date, date_str)
    if not match:
        return False

    # Дополнительные проверки на валидность значений
    year = int(match.group('year'))
    month = int(match.group('month'))
    day = int(match.group('day'))
    hour = int(match.group('hour'))
    minute = int(match.group('minute'))
    second = int(match.group('second'))

    # Проверка диапазонов
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False
    if hour < 0 or hour > 23:
        return False
    if minute < 0 or minute > 59:
        return False
    if second < 0 or second > 59:
        return False

    return True


if __name__ == "__main__":
    print(mask_account_card("Visa Classic 6831982476737658"))
    print(get_date("2024-03-11T02:26:18.671407"))
