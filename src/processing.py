import re



def filter_by_state(data: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """ Функция принимает список словарей и возвращает список словарей соответствующих состоянию state"""
    result = []
    for element in data:
        if element['state'] == state:
            result.append(element)
    return result


def sort_by_date(data: list[dict], reverse_option: bool = True) -> list[dict]:
    """Функция сортирует список словарей по дате"""
    return sorted(data, key=lambda x: x['date'], reverse=reverse_option)


def filter_by_description(transactions: list[dict], search_str: str) -> list[dict]:
    """
    Функция принимает список транзакций transactions и строку поиска search_str,
    возвращает список транзакций, у которых описание содержит строку поиска
    """
    search_pattern = rf".*{search_str.lower()}.*"
    search_reg = re.compile(pattern=search_pattern, flags=re.IGNORECASE)
    result = []

    for transaction in transactions:
        description = transaction.get("description","").lower()
        if search_reg.match(description):
            result.append(transaction)

    return result
