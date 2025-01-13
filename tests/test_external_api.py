from unittest.mock import patch

import pytest
import requests

from src.external_api import get_sum_transit


@patch('requests.get')
def test_get_sum_transit(mock_get, my_transaction):
    mock_get.return_value.json.return_value = {'success': True, 'query': {'from': 'EUR', 'to': 'RUB', 'amount': 1000},
                                               'info': {'timestamp': 1736152444, 'rate': 111.66293},
                                               'date': '2025-01-06', 'result': 111662.93}
    assert (get_sum_transit(my_transaction)) == 111662.93


def test_get_sum_transit_invalid_data():
    with pytest.raises(ValueError):
        get_sum_transit('')


def test_get_sum_transit_type_data():
    with pytest.raises(TypeError):
        get_sum_transit(10)


def test_get_sum_transit_key_error(my_transaction_no_operation):
    with pytest.raises(KeyError):
        get_sum_transit(my_transaction_no_operation)


@patch('requests.get')
def test_get_sum_transit_usd(mock_get, my_transaction_usd):
    mock_get.return_value.json.return_value = {'success': True,
                                               'query': {'from': 'USD', 'to': 'RUB', 'amount': 8220.37},
                                               'info': {'timestamp': 1736177704, 'rate': 107.510861},
                                               'date': '2025-01-06', 'result': 883779.056439}
    assert get_sum_transit(my_transaction_usd) == 883779.056439
