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


@pytest.mark.parametrize("card_number_invalid_type", [1234,
                                                      True,
                                                      [1,2],
                                                      {}])


def test_get_mask_card_number_invalid_type(card_number_invalid_type):
    with pytest.raises(TypeError):
        get_mask_card_number(card_number_invalid_type)


@pytest.mark.parametrize("card_number_invalid_format", ["1234",
                                                        "asdf 1234 assdf 3214fsd"
                                                        ""
                                                        "1234456677888854"])


def test_get_mask_card_number_invalid_format(card_number_invalid_format):
    with pytest.raises(ValueError):
        get_mask_card_number(card_number_invalid_format)