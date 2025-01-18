import pytest
from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    assert get_mask_card_number("1234567898765432") == "1234 56** **** 5432"


def test_get_mask_account():
    assert get_mask_account("123456789987654321") == "**4321"


@pytest.mark.parametrize("invalid_card_type", [1234,
                                               True,
                                               [1,2],
                                               {}])


def test_get_mask_card_number_invalid_type(invalid_card_type):
    with pytest.raises(TypeError):
        get_mask_card_number(invalid_card_type)


@pytest.mark.parametrize("invalid_card_format", ["1234",
                                                 "asdf 1234 assdf 3214fsd",
                                                 "",
                                                 "12344566778888541"])


def test_get_mask_card_number_invalid_format(invalid_card_format):
    with pytest.raises(ValueError):
        get_mask_card_number(invalid_card_format)


@pytest.mark.parametrize("invalid_account_type", [1234,
                                                  True,
                                                  [1,2],
                                                  {}])


def test_get_mask_account_invalid_type(invalid_account_type):
    with pytest.raises(TypeError):
        get_mask_account(invalid_account_type)



@pytest.mark.parametrize("invalid_account_format", ["1234",
                                                    "asdf 1234 assdf 3214fsd",
                                                    "",
                                                    "123445667788885445678978945"])


def test_get_mask_account_invalid_format(invalid_account_format):
    with pytest.raises(ValueError):
        get_mask_account(invalid_account_format)
