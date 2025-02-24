from unittest.mock import patch

from src.external_api import convert_amount_by_currency


@patch("requests.request")
def test_convert_amount_by_currency(mock_request):
    mock_response = mock_request.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": "822137"}
    assert convert_amount_by_currency("USD", "RUB", 8221.37) == 822137
