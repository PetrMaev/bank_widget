from unittest.mock import mock_open, patch

import pytest

from src.utils import read_json


def test_get_transit_info():
    mocked_open = mock_open(read_data='[{"id": 1, "amount": "100.0"}]')

    with patch('builtins.open', mocked_open):
        result = read_json(r'..\data\operations.json')
        assert result == [{"id": 1, "amount": "100.0"}]


def test_get_transit_info_invalid_json_file(capsys):
    mocked_open = mock_open(read_data='0x00')
    with patch('builtins.open', mocked_open):
        read_json(' ')
        captured = capsys.readouterr()
        assert captured.out == 'Ошибка декодирования файла\n'


def test_get_transit_info_data_error():
    with pytest.raises(ValueError):
        read_json('')


def test_get_transit_info_invalid_data():
    with pytest.raises(TypeError):
        read_json(1)
