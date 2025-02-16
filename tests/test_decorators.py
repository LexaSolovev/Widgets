from src.decorators import log
from os import remove

def test_log_console(capsys):
    @log()
    def summator(*args):
        return sum(args)

    result = summator(1, 2, 3, 4)
    str_in_console = capsys.readouterr()
    assert result == 10
    assert "Начало запуска функции summator:" in str_in_console.out
    assert "Функция выполнена успешно за" in str_in_console.out
    assert "Результат выполнения функции:" in str_in_console.out


def test_log_console_except(capsys):
    @log()
    def exeptor():
        raise Exception("Тестовая ошибка")


    try:
        exeptor()
    except:
        assert "При выполнении функции exeptor c параметрами () произошла ошибка:\nТестовая ошибка" in capsys.readouterr().out


def test_log_file():
    @log("temp.txt")
    def summator(*args):
        return sum(args)


    result = summator(1, 2, 3, 4)
    with open("temp.txt", "r") as file:
        str_in_file = file.read()
        assert result == 10
        assert "Начало запуска функции summator:" in str_in_file
        assert "Функция выполнена успешно за" in str_in_file
        assert "Результат выполнения функции:" in str_in_file
    remove("temp.txt")
