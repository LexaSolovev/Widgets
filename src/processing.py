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
