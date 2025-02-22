from unittest.mock import Mock

import src.utils
from src.utils import get_amount


def test_get_amount_usd():
    mock_amount = Mock(return_value=822137.0)
    src.utils.convert_amount_by_currency = mock_amount
    assert get_amount(
        {
            "operationAmount":
                {
                    "amount": "8221.37",
                    "currency":
                        {
                            "name": "USD",
                            "code": "USD"
                        }
                }
        }
    ) == 822137.0


def test_get_amount_rub():
    mock_amount = Mock(return_value=822137.0)
    src.utils.convert_amount_by_currency = mock_amount
    assert get_amount(
        {
            "operationAmount":
                {
                    "amount": "8221.37",
                    "currency":
                        {
                            "name": "RUB",
                            "code": "RUB"
                        }
                }
        }
    ) == 8221.37
