import pytest
from src.widget import mask_account_card, get_date, is_valid_datetime

@pytest.fixture
def account():
    return "Счет 736541084301358743"


def test_mask_account_card_valid_account(account):
    assert mask_account_card(account) == "Счет **8743"


@pytest.mark.parametrize("card_number, expected", [("Master Card 1234 5678 9876 5432", "Master Card 1234 56** **** 5432"),
                                                   ("Visa 1234567898765432", "Visa 1234 56** **** 5432"),
                                                   ("UnionPay 1234567898765432", "UnionPay 1234 56** **** 5432"),
                                                   ("Мир 1234 5678 9876 5432", "Мир 1234 56** **** 5432")])


def test_mask_account_card_valid_card(card_number, expected):
    assert mask_account_card(card_number) == expected

@pytest.mark.parametrize("invalid_type", [True,
                                          1234,
                                          (1,2),
                                          {3:5},
                                          [4,1]])


def test_mask_account_card_invalid_type(invalid_type):
    with pytest.raises(TypeError):
        mask_account_card(invalid_type)


@pytest.mark.parametrize("invalid_format", ["1234562345",
                                            "Счет 12345",
                                            "Visa 1234567891",
                                            "",
                                            "Master Card 123",
                                            " 1234567898765432"])


def test_mask_account_invalid_format(invalid_format):
    with pytest.raises(ValueError):
        mask_account_card(invalid_format)


@pytest.fixture
def date():
    return ("2024-03-11T02:26:18.671407")

def test_get_date(date):
    assert get_date(date) == "11.03.2024"


@pytest.mark.parametrize("invalid_type", [True,
                                          1234,
                                          (1,2),
                                          {3:5},
                                          [4,1]])


def test_get_date_invalid_type(invalid_type):
    with pytest.raises(TypeError):
        get_date(invalid_type)


def test_is_valid_datetime(date):
    assert is_valid_datetime(date) == True


@pytest.mark.parametrize("invalid_datetime", ["2024-03-11T02:26:18",
                                              "03-11T02:26:18.671407",
                                              "2024-11T02:26:18.671407",
                                              "2024-03-T02:26:18.671407",
                                              "2024-03-11T:26:18.671407",
                                              "2024-03-11T02::18.671407",
                                              "2024-03-11T02:26:"
                                              "2024-03-11"
                                              "0024-03-11T02:26:18.671407",
                                              "2024-13-11T02:26:18.671407",
                                              "2024-03-00T02:26:18.671407",
                                              "2024-03-32T02:26:18.671407",
                                              "2024-03-11T24:26:18.671407",
                                              "2024-03-11T02:60:18.671407",
                                              "2024-03-11T02:26:60.671407",
                                              "2024-03-11T02:26:18.6714071"])
def test_is_valid_datetime(invalid_datetime):
    assert is_valid_datetime(invalid_datetime) == False


@pytest.mark.parametrize("invalid_datetime", ["2024-03-11T02:26:18",
                                              "03-11T02:26:18.671407",
                                              "2024-11T02:26:18.671407",
                                              "2024-03-T02:26:18.671407",
                                              "2024-03-11T:26:18.671407",
                                              "2024-03-11T02::18.671407",
                                              "2024-03-11T02:26:"
                                              "2024-03-11"
                                              "0024-03-11T02:26:18.671407",
                                              "2024-13-11T02:26:18.671407",
                                              "2024-03-00T02:26:18.671407",
                                              "2024-03-32T02:26:18.671407",
                                              "2024-03-11T24:26:18.671407",
                                              "2024-03-11T02:60:18.671407",
                                              "2024-03-11T02:26:60.671407",
                                              "2024-03-11T02:26:18.6714071"])
def test_get_date(invalid_datetime):
    with pytest.raises(ValueError):
        get_date(invalid_datetime)