import pytest
from mock import patch
from main import Card, Comp, Human, Game


@pytest.mark.parametrize('num_menu, p1, p2', (['1', Human, Comp], ['2', Human, Human], ['3', Comp, Comp]))
def test_start(num_menu, p1, p2):
    with patch('builtins.input', lambda x: num_menu):
        game = Game()
        assert isinstance(game.player1, p1) and isinstance(game.player2, p2)


@pytest.fixture
def fix5():
    p1 = Comp()
    p1.name = 'First'
    p1.card = Card()
    p1.card.card = [['#', '#', '#', 30, '#', '#', '#', '#', '#', '#'],
                    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]
    p2 = Comp()
    p2.name = 'Second'
    p2.card = Card()
    p2.card.card = [['#', '#', 20, '#', '#', '#', '#', '#', '#', '#'],
                    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]
    with patch('builtins.input', lambda x: '3'):
        game = Game()
    game.player1 = p1
    game.player2 = p2
    return game


@pytest.mark.parametrize('num, ans, not_ans', ([30, 'First', 'Second'], [20, 'Second', 'First']))
def test_exit(fix5, num, ans, not_ans):
    fix5.bag = [num]
    fix5.start()
    assert fix5.winner == ans and fix5.loser == not_ans, 'Ошибка результата'