from random import sample
import pytest
from main import Card


@pytest.mark.parametrize('arg', range(5))
def test_create(arg):
    new_card = Card()
    eq = set()
    for item in new_card.card:
        eq |= set(item)
    new_card = eq - {'#'}
    assert len(new_card) == 15, 'Ошибка карточки'


@pytest.fixture
def fixer():
    result = Card()
    result.card = [sample(['#', '-'], counts=[15, 15], k=10) for _ in range(3)]
    print(result)
    return result


def test_empty(fixer):
    card = fixer
    assert card.is_empty, "Непустая карточка"


def test_not_empty():
    new_card = Card()
    assert not new_card.is_empty, 'Пустая карточка'


@pytest.fixture
def fix1():
    card = Card()
    card.card = ['#'] * 9 + [5]
    card.card = [card.card for _ in range(3)]
    return card


@pytest.fixture
def fix2():
    card = Card()
    card.card = ['#'] * 10
    card.card = [card.card for _ in range(3)]
    return card


def test_number_in_list(fix1, fix2):
    assert fix1.is_num_to_card(5), '5 не в карте'
    assert not fix2.is_num_to_card(5), '5 в карте'


@pytest.fixture
def fix3():
    card = Card()
    card.card = [[1, 10, 20, 30, 40, 'x', 'x', 'x', 'x', 'x'],
                 [2, 11, 21, 31, 41, 'x', 'x', 'x', 'x', 'x'],
                 [3, 12, 22, 32, 42, 'x', 'x', 'x', 'x', 'x']]
    return card


def test_find_num(fix3):
    true_card = [[1, 10, 20, 30, 40, 'x', 'x', 'x', 'x', 'x'],
                 [2, 11, '-', 31, 41, 'x', 'x', 'x', 'x', 'x'],
                 [3, 12, 22, 32, 42, 'x', 'x', 'x', 'x', 'x']]
    fix3.cross_out(21)
    assert fix3.card == true_card, "Удаление цифры не работает"


def test_equal():
    card1 = Card()
    card1.card = [['#', '#', '#', 30, '#', '#', '#', '#', '#', '#'],
                  ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                  ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]
    card2 = Card()
    card2.card = [['#', '#', '#', 30, '#', '#', '#', '#', '#', '#'],
                  ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                  ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]
    assert card1 == card2, "Карты не равны"