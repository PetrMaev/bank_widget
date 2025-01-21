from unittest.mock import mock_open, patch

from src.read_files import read_csv, read_excel


@patch('pandas.read_csv')
def test_read_csv(mock_read_csv):
    mock_read_csv.return_value.to_dict.return_value = [
        {'id': 1111, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 1111, 'currency_name': 'Testname',
         'currency_code': 'PEN', 'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397',
         'description': 'test'}]
    assert read_csv("path_csv_test_file") == [
        {'id': 1111, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 1111, 'currency_name': 'Testname',
         'currency_code': 'PEN', 'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397',
         'description': 'test'}]


@patch('pandas.read_excel')
def test_read_excel(mock_read_excel):
    mock_read_excel.return_value.to_dict.return_value = [
        {'id': 1111, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 1111, 'currency_name': 'Testname',
         'currency_code': 'PEN', 'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397',
         'description': 'test'}]
    assert read_excel("path_excel_test_file") == [
        {'id': 1111, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 1111, 'currency_name': 'Testname',
         'currency_code': 'PEN', 'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397',
         'description': 'test'}]
    mock_read_excel.assert_called_once_with("path_excel_test_file")
