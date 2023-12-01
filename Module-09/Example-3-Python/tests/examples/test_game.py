import copy

import pytest
from hamcrest import *

from examples import Board, Game, Player, Referee

"""
1 - Does this piece of code perform the operations
    it was designed to perform?

2 - Does this piece of code do something it was not
    designed to perform?

1 Test per mutator
"""


@pytest.fixture
def empty_board():
    yield Board()


@pytest.fixture
def players_and_game():
    tom = Player("Tom")
    a_cylon = Player()

    a_game = Game(tom, a_cylon)

    yield tom, a_cylon, a_game


def test_constructor(empty_board, players_and_game):
    tom, a_cylon, a_game = players_and_game

    assert_that(a_game.get_player1(), equal_to(tom))
    assert_that(a_game.get_player2(), equal_to(a_cylon))

    assert_that(a_game.get_player1().get_symbol(), is_("X"))
    assert_that(a_game.get_player2().get_symbol(), is_("O"))

    assert_that(a_game.is_over(), is_(False))

    assert_that(a_game.get_winner(), is_(none()))
    assert_that(a_game.get_loser(), is_(none()))

    # Can not test without Board.equals method
    assert_that(a_game.get_board(), equal_to(empty_board))


@pytest.mark.skip(reason="can **not** test")
def test_play_round():
    # Can not test due to hardcoded System.in use in Player.next_move
    pass
