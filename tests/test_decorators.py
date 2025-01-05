import os

import pytest

from src.decorators import log
from config import path


def test_log():
    @log(filename='my_log')
    def example_function(a, b):
        """ Складывает два числа"""
        return a + b

    example_function(1, 2)
    with open(os.path.join(path, 'my_log.txt'), 'r', encoding='utf-8') as file:
        data = file.read().split('\n')
    assert data[-2] == 'example_function ok'


def test_log_invalid_data():
    @log(filename='my_log')
    def example_function(a, b):
        """ Складывает два числа"""
        return a + b

    example_function()
    with open(os.path.join(path, 'my_log.txt'), 'r', encoding='utf-8') as file:
        data = file.read().split('\n')
    assert data[-2] == 'example_function error: TypeError. Inputs: (), {}'


def test_log_console(capsys):
    @log(filename=None)
    def example_function(a, b):
        """ Складывает два числа"""
        return a + b

    example_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == 'example_function ok\n'


def test_log_console_2(capsys):
    @log(filename=None)
    def example_function(a, b):
        """ Складывает два числа"""
        return a + b

    example_function()
    captured = capsys.readouterr()
    assert captured.out == 'example_function error: TypeError. Inputs: (), {}\n\n'
