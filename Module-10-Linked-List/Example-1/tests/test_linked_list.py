import copy
from dataclasses import dataclass
from typing import Any

import pytest
from hamcrest import *

from linkedlist import LinkedList


@pytest.fixture()
def build_interesting_list():
    ll = LinkedList()

    some_ints = list(range(1, 5))
    some_strings = ["Hello", "Python", "Hi"]

    data_to_add = some_ints + some_strings

    for val in data_to_add:
        ll.append(val)

    yield data_to_add, ll


def test_constructor():
    empty_list = LinkedList()

    assert_that(empty_list, is_(not_none()))
    assert_that(empty_list, has_length(0))
    assert_that(empty_list, has_string(""))


def test_append_int_once():
    ll = LinkedList()
    ll.append(1)

    assert_that(ll, has_length(1))
    assert_that(ll, has_string("Node #0 contains 1\n"))


def test_append_int_twice():
    ll = LinkedList()
    ll.append(2)
    ll.append(3)

    assert_that(ll, has_length(2))

    # Check __str__
    expected_strs = [
        f"Node #{idx} contains {datum}" for idx, datum in enumerate(range(2, 4))
    ]
    assert_that(str(ll), string_contains_in_order(*expected_strs))


def test_append_various(build_interesting_list):
    all_src_data, ll = build_interesting_list

    assert_that(ll, is_(instance_of(LinkedList)))
    assert_that(ll, has_length(len(all_src_data)))


def test_str_after_append_various(build_interesting_list):
    all_src_data, ll = build_interesting_list

    expected_strs = [
        f"Node #{idx} contains {datum}" for idx, datum in enumerate(all_src_data)
    ]
    assert_that(str(ll), string_contains_in_order(*expected_strs))

