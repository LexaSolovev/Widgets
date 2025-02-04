from src.decorators import log

def test_log_console(capsys):
    @log()
    def summator(*args):
        return sum(args)

    summator(1, 2, 3, 4)
    str_in_console = capsys.readouterr()
    assert "Начало запуска функции summator:" in str_in_console.out
    assert "Функция выполнена успешно за" in str_in_console.out
    assert "Результат выполнения функции:" in str_in_console.out

