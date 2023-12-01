import copy

import pytest
from hamcrest import *

from examples.board import Board

"""
1 - Does this piece of code perform the operations
    it was designed to perform?

2 - Does this piece of code do something it was not
    designed to perform?

1 Test per mutator
"""

EXPECTED_EMPTY_STRING = "1|2|3\n4|5|6\n7|8|9"


@pytest.fixture
def a_board():
    yield Board()


def test_default_constructor(a_board):
    for expected_char in range(1, 10):
        assert_that(a_board.get_cell(expected_char), is_(str(expected_char)))

    assert_that(str(a_board), equal_to(EXPECTED_EMPTY_STRING))
    assert_that(a_board.is_full(), is_(False))

    retrieved = a_board.get_3_cells(1, 2, 3)
    expected = ((0, "1"), (1, "2"), (2, "3"))

    assert_that(retrieved[0], equal_to(expected[0]))
    assert_that(retrieved[1], equal_to(expected[1]))
    assert_that(retrieved[2], equal_to(expected[2]))


def test_set_cell(a_board):
    a_board.set_cell(1, "X")
    a_board.set_cell(9, "O")

    assert_that(a_board.get_cell(1), is_("X"))
    assert_that(a_board.get_cell(9), is_("O"))

    retrieved = a_board.get_3_cells(1, 5, 9)
    expected = ((0, "X"), (4, "5"), (8, "O"))

    assert_that(retrieved[0], equal_to(expected[0]))
    assert_that(retrieved[1], equal_to(expected[1]))
    assert_that(retrieved[2], equal_to(expected[2]))

    assert_that(str(a_board), is_not(equal_to(EXPECTED_EMPTY_STRING)))
    assert_that(str(a_board), equal_to("X|2|3\n4|5|6\n7|8|O"))

    assert_that(a_board.is_full(), is_(False))
