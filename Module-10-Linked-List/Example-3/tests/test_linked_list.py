import copy
import random
from dataclasses import dataclass
from typing import Any

import pytest
from hamcrest import *

from linkedlist import LinkedList


@dataclass
class Datum:
    """
    This class exists to test the linked list __deepcopy__ due to how int and
    str "objects" are immutable
    """

    val: Any


@pytest.fixture()
def build_interesting_list():
    some_ints = list(range(1, 5))
    some_strings = ["Hello", "Python", "Hi"]

    data_to_add = some_ints + some_strings

    ll = LinkedList(data_to_add)

    yield data_to_add, ll


def test_constructor_empty_list():
    empty_list = LinkedList()

    assert_that(empty_list, is_(not_none()))
    assert_that(empty_list, has_length(0))
    assert_that(empty_list, has_string("LinkedList()"))


def test_iterator_empty_list():
    empty_list = LinkedList()
    it = iter(empty_list)

    with pytest.raises(StopIteration) as _err:
        next(it)


def test_equality_empty_list():
    ll_1 = LinkedList()
    ll_2 = LinkedList()

    # A list should always be equal to itself
    assert_that(ll_1, is_(equal_to(ll_1)))

    # Two empty lists should be equal
    assert_that(ll_1, is_(equal_to(ll_2)))


def test_append_int_once():
    ll = LinkedList()
    ll.append(1)

    assert_that(ll, has_length(1))
    assert_that(ll, has_string("LinkedList((1))"))


def test_iterator_append_int_once():
    ll = LinkedList()
    ll.append(1)

    it = iter(ll)
    val = next(it)

    assert_that(val, is_(instance_of(int)))
    assert_that(val, is_(equal_to(1)))

    # Check that we have exhausted the list
    with pytest.raises(StopIteration) as _err:
        next(it)


def test_append_int_twice():
    ll = LinkedList()
    ll.append(2)
    ll.append(3)

    assert_that(ll, has_length(2))

    # Check __repr__
    expected_strs = [
        f"{datum!r}" for datum in range(2, 4)
    ]
    assert_that(str(ll), string_contains_in_order(*expected_strs))


def test_iterator_append_int_twice():
    ll = LinkedList()
    ll.append(2)
    ll.append(3)

    it = iter(ll)

    val = next(it)
    assert_that(val, is_(instance_of(int)))
    assert_that(val, is_(equal_to(2)))

    val = next(it)
    assert_that(val, is_(instance_of(int)))
    assert_that(val, is_(equal_to(3)))

    # Check that we have exhausted the list
    with pytest.raises(StopIteration) as _err:
        next(it)


def test_equality_int_twice():
    ll_1 = LinkedList()
    ll_1.append(2)
    ll_1.append(3)

    ll_2 = LinkedList()
    ll_2.append(1)
    ll_2.append(3)

    assert_that(ll_1, is_(equal_to(ll_1)))
    assert_that(ll_1, is_(not_(equal_to(ll_2))))


def test_equality_int_different_lengths():
    ll_1 = LinkedList((3,))
    ll_2 = LinkedList((1, 3))

    assert_that(ll_1, is_(equal_to(ll_1)))
    assert_that(ll_1, is_(not_(equal_to(ll_2))))


def test_append_various(build_interesting_list):
    all_src_data, ll = build_interesting_list

    assert_that(ll, is_(instance_of(LinkedList)))
    assert_that(ll, has_length(len(all_src_data)))


def test_equality_various(build_interesting_list):
    all_src_data, ll_1 = build_interesting_list

    # Shuffle source data
    random.shuffle(all_src_data)
    shuffled_data = all_src_data

    # Create a second list with the same data in a different order
    ll_2 = LinkedList()
    for val in shuffled_data:
        ll_2.append(val)

    assert_that(ll_1, is_(equal_to(ll_1)))
    assert_that(ll_1, is_(not_(equal_to(ll_2))))


def test_str_after_append_various(build_interesting_list):
    all_src_data, ll = build_interesting_list

    expected_strs = [
        f"{datum!r}" for datum in all_src_data
    ]
    assert_that(str(ll), string_contains_in_order(*expected_strs))


def test_deep_copy_empty():
    empty_list = LinkedList()
    cpy_list = copy.deepcopy(empty_list)

    assert_that(cpy_list, is_(equal_to(empty_list)))
    assert_that(cpy_list, is_(not_(same_instance(empty_list))))

    cpy_list.append(7)
    assert_that(empty_list, has_length(0))
    assert_that(cpy_list, has_length(1))


def test_deep_copy_with_data(build_interesting_list):
    all_src_data, ll_src = build_interesting_list

    ll_src.extend(Datum(val) for val in (52, 42, 337))

    ll_copy = copy.deepcopy(ll_src)

    assert_that(ll_copy, is_(instance_of(LinkedList)))

    assert_that(ll_copy, has_length(len(ll_src)))

    for val_copy, val_src in zip(ll_copy, ll_src):
        assert_that(val_copy, is_(equal_to(val_src)))

        # Skip int and str entries... literals will always be the same object
        if any(isinstance(val_copy, a_type) for a_type in [int, str]):
            continue

        #  print(val_copy)
        assert_that(val_copy, is_(not_((same_instance(val_src)))))

    expected_repr = "LinkedList((" + ", ".join(repr(datum) for datum in ll_copy) + "))"
    assert_that(repr(ll_copy), equal_to(expected_repr))


def test_constructor_from_range():
    ll = LinkedList(range(1, 9))

    assert_that(ll, is_(instance_of(LinkedList)))

    assert_that(ll, has_length(8))

    for val, val_src in zip(ll, range(1, 9)):
        assert_that(val, is_(equal_to(val_src)))

    expected_repr = "LinkedList((" + ", ".join(repr(datum) for datum in ll) + "))"
    assert_that(repr(ll), equal_to(expected_repr))


def test_add():
    ll_lhs = LinkedList(range(1, 100))
    ll_rhs = LinkedList(Datum(val) for val in range(2, 100, 2))
    a_list = [Datum("Hello!")]

    ll_combined = ll_lhs + ll_rhs + a_list

    assert_that(ll_combined, is_(not_(same_instance(ll_lhs))))
    assert_that(ll_combined, is_(not_(same_instance(ll_rhs))))

    combined_data = list(ll_lhs) + list(ll_rhs) + a_list

    assert_that(ll_combined, has_length(len(combined_data)))
    assert_that(ll_combined, contains_exactly(*combined_data))


def test_contains():
    ll = LinkedList(Datum(val) for val in range(2, 100, 2))

    assert_that(Datum(2) in ll)
    assert_that(Datum(20) in ll)
    assert_that(Datum(98) in ll)

    assert_that(Datum(100) not in ll)
    assert_that(Datum(122) not in ll)

