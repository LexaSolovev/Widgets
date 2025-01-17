import pytest
from src.widget import mask_account_card

@pytest.fixture
def card():
    return "Visa Platinum 7000792289606361"


@pytest.fixture
def account():
    return "Счет 736541084301358743"


def test_mask_account_card_valid_card(card):
    assert mask_account_card(card) == "Visa Platinum 7000 79** **** 6361"


def test_mask_account_card_valid_account(account):
    assert mask_account_card(account) == "Счет **8743"