import pytest
from src.widget import mask_account_card

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