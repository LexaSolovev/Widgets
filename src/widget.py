import masks


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
    data_list = data.split()
    iscard = bool(len(data_list[-1]) == 16)
    if iscard:
        data_list[-1] = masks.get_mask_card_number(data_list[-1])
    else:
        data_list[-1] = masks.get_mask_account(data_list[-1])
    return " ".join(data_list)


if __name__ == "__main__":
    print(mask_account_card("Visa Classic 6831982476737658"))
