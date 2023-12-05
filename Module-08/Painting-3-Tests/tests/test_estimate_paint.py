import pytest

from hamcrest import *

from estimate_paint import get_report


def test_get_report_equal_min_max():
    actual_report = get_report(min_gallons=4, max_gallons=4, price_per_gallon=35.10)

    assert_that(actual_report, contains_string("4"))
    assert_that(actual_report, contains_string("140.40"))

    assert_that(
        actual_report,
        string_contains_in_order(
            "You will need to buy "
            "4",
            " gallons of paint.",
            "\n",
            "You will spend",
            "$ 140.40."
        )
    )


def test_get_report_different_min_max():
    actual_report = get_report(min_gallons=10, max_gallons=14, price_per_gallon=32.50)

    assert_that(
        actual_report,
        string_contains_in_order(
            "You will need to buy "
            "10 to 14",
            " gallons of paint.",
            "\n",
            "You will spend",
            "$ 325.00 to $ 455.00."
        )
    )
