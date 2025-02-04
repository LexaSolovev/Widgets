from functools import wraps
from time import time
from typing import Callable
from datetime import datetime

def log(file_name: str="") -> Callable:
    def inner(func):
        def write_to_log(log_str: str, name_of_file:str = ""):
            if file_name == "":
                print(log_str,end="")
            else:
                with open(file_name, "a", encoding="UTF-8") as log_file:
                    log_file.write(log_str + "\n")


        @wraps(func)
        def wrapper(*args, **kwargs):
            write_to_log(f"Начало запуска функции {func.__name__}: {str(datetime.now())}\n", name_of_file=file_name)
            start = time()
            try:
                result = func(*args,**kwargs)
            except Exception as exept:
                write_to_log(f"При выполнении функции {func.__name__} c параметрами {args} произошла ошибка:\n" + str(exept), name_of_file=file_name)
                raise exept
            else:
                stop = time()
                write_to_log(f"Функция выполнена успешно за {stop - start} секунд\n", name_of_file=file_name)
                write_to_log(f"Результат выполнения функции:\n{result}", name_of_file=file_name)
                return result

        return wrapper

    return inner
