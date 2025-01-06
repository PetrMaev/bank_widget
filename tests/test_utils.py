import pytest
from unittest.mock import mock_open, patch
import json

from src.utils import get_transit_info


def test_get_transit_info():
    mocked_open = mock_open(read_data='[{"id": 1, "amount": "100.0"}]')

    with patch('builtins.open', mocked_open):
        result = get_transit_info(r'..\data\operations.json')
        assert result == [{"id": 1, "amount": "100.0"}]


def test_get_transit_info_invalid_json_file():
    mocked_open = mock_open(read_data='[{id: 1, "amount": "100.0"}]')
    with patch('builtins.open', mocked_open):
        result = get_transit_info(r'..\data\operations.json')


def test_get_transit_info_data_error():
    with pytest.raises(ValueError):
        get_transit_info('')


def test_get_transit_info_invalid_data():
    with pytest.raises(TypeError):
        get_transit_info(1)
