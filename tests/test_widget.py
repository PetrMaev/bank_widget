import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize('account_card, expected', [('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361'),
                                                    ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
                                                    ('7158300734726758', '7158 30** **** 6758'),
                                                    ('Счет 64686473678894779589', 'Счет **9589'),
                                                    ('35383033474447895560', '**5560')
                                                    ])

def test_mask_account_card(account_card, expected) -> None:
    assert mask_account_card(account_card) == expected


def test_mask_account_card_invalid_data():
    with pytest.raises(ValueError):
        mask_account_card('456512321')


def test_mask_account_card_invalid_type():
    with pytest.raises(TypeError):
        mask_account_card(23569821255)


@pytest.mark.parametrize('date, expected', [('2024-03-11T02:26:18.671407', '11.03.2024'),
                                            ('2019-07-03T18:35:29.512364', '03.07.2019'),
                                            ('2018-06-30T02:08:58.425572', '30.06.2018'),
                                            ('2018-09-12T21:27:25.241689', '12.09.2018'),
                                            ])
def test_get_date(date, expected) -> None:
    assert get_date(date) == expected


def test_get_date_invalid_data():
    with pytest.raises(ValueError):
        get_date('2024-03-1102:26:18.671407')