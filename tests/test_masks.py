import pytest
from src.masks import get_mask_account, get_mask_card_number

@pytest.fixture
def card_number():
    return "1234 5678 9876 5432"

@pytest.fixture
def account():
    return "1234567898765432"

def test_get_mask_card_number(card_number):
    assert get_mask_card_number(card_number) == "1234 56** **** 5432"


def test_get_mask_account(account):
    assert get_mask_account(account) == "**5432"