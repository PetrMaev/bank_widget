from typing import Any

import pytest

from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number() -> None:
    assert get_mask_card_number(7000792289606361) == "7000 79** **** 6361"


def test_get_mask_card_number_invalid_data() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(7)


def test_get_mask_card_number_invalid_type() -> None:
    with pytest.raises(TypeError):
        get_mask_card_number("7000792289606361")


def test_get_mask_account() -> None:
    assert get_mask_account(73654108430135874305) == "**4305"


def test_get_mask_account_invalid_data() -> None:
    with pytest.raises(ValueError):
        get_mask_account(736)


def test_get_mask_account_invalid_type() -> None:
    with pytest.raises(TypeError):
        get_mask_account("7000792289606361")
