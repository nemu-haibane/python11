import pytest
import mock
from main import Comp, Card, Human


@pytest.fixture
def fix3():
    card = Card()
    card.card = [[1, 10, 20, 30, 40, '#', '#', '#', '#', '#'],
                 [2, 11, 21, 31, 41, '#', '#', '#', '#', '#'],
                 [3, 12, 22, 32, 42, '#', '#', '#', '#', '#']]
    return card


def test_comp_step(fix3):
    human = Comp()
    human.card = fix3
    assert human.step(10), 'Error step'
    assert human.step(51) is True, 'OverTime'


@pytest.mark.parametrize('num, y, result', ([21, 'д', True], [21, 'н', False], [51, 'д', False], [51, 'н', True]))
def test_human_step(fix3, num, y, result):
    with mock.patch('builtins.input', lambda x: y):
        human = Human()
        human.card = fix3
        assert human.step(num) is result, 'Error'


@pytest.fixture
def fix4():
    card = Card()
    card.card = [[1, 14, 22, 32, 40, 51, '#', 76, 86, 95],
                 ['#', '#', 29, 33, 41, 53, '#', '#', '#', '#'],
                 ['#', '#', '#', '#', 43, 52, '#', '#', '#', '#']]
    return card


def test_comp_step1(fix4):
    test_card = [[1, 14, 22, '-', 40, 51, '#', 76, 86, 95],
                 ['#', '#', 29, 33, 41, 53, '#', '#', '#', '#'],
                 ['#', '#', '#', '#', 43, 52, '#', '#', '#', '#']]
    comp = Comp()
    comp.card = fix4
    comp.step(32)
    assert comp.card.card == test_card, 'Error'
    comp.step(34)
    assert comp.card.card == test_card, 'Error'


def test_comp_num(fix4):
    comp = Comp()
    comp.card = fix4
    assert comp.card.is_num_to_card(32), "Есть номер"
    assert not comp.card.is_num_to_card(34), "Нет номера"