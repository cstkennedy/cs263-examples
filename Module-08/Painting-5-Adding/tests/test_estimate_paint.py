from io import StringIO

import pytest
from hamcrest import assert_that, close_to, contains_string, string_contains_in_order

from estimate_paint import gather_input, get_report


def test_gather_input_cli_arg():
    length, width, unit_cost = gather_input([None, "40", "50", "49.95"])
    assert_that(length, close_to(40, 1e-3))
    assert_that(width, close_to(50, 1e-3))
    assert_that(unit_cost, close_to(49.95, 1e-3))


def test_gather_input_input(monkeypatch):
    faked_input = StringIO("40\n50\n49.95\n")
    monkeypatch.setattr("sys.stdin", faked_input)

    length, width, unit_cost = gather_input([])
    assert_that(length, close_to(40, 1e-3))
    assert_that(width, close_to(50, 1e-3))
    assert_that(unit_cost, close_to(49.95, 1e-3))


def test_get_report_equal_min_max():
    actual_report = get_report(min_gallons=4, max_gallons=4, price_per_gallon=35.10)

    assert_that(actual_report, contains_string("4"))
    assert_that(actual_report, contains_string("140.40"))

    assert_that(
        actual_report,
        string_contains_in_order(
            "You will need to buy ",
            "4",
            " gallons of paint.",
            "\n",
            "You will spend",
            "$ 140.40.",
        ),
    )


def test_get_report_different_min_max():
    actual_report = get_report(min_gallons=10, max_gallons=14, price_per_gallon=32.50)

    assert_that(
        actual_report,
        string_contains_in_order(
            "You will need to buy ",
            "10 to 14",
            " gallons of paint.",
            "\n",
            "You will spend",
            "$ 325.00 to $ 455.00.",
        ),
    )
