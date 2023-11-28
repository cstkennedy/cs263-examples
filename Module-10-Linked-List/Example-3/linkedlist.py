from __future__ import annotations

import collections.abc
import copy
from dataclasses import dataclass
from typing import Any, Self


class LinkedList(collections.abc.Iterable):
    @dataclass
    class Node:
        data: Any = None
        next_node: Self = None

    class Iterator(collections.abc.Iterator):
        def __init__(self, starting_node=None):
            self.current_node = starting_node

        def __next__(self):
            if not self.current_node:
                raise StopIteration()

            value = self.current_node.data

            # Move to the next node
            self.current_node = self.current_node.next_node

            return value

    def __init__(self, initial_data: collections.abc.Iterable = None):
        self.head: LinkedList.Node = None
        self.tail: LinkedList.Node = None
        self.length: int = 0  # Do not include the "buffer" Node

        new_node = LinkedList.Node(data=None)

        self.head = new_node
        self.tail = new_node

        # Use extend to add any starting data
        if initial_data:
            self.extend(initial_data)

    def append(self, val: Any) -> None:
        """
        Add a piece of data (entry) to the end of the list. If the list is
        currently empty, this new entry will be both the first and last entry
        in the list.

        Args:
            val: piece of data to store
        """

        new_node = LinkedList.Node(val)

        # Add the new node after the current tail
        self.tail.next_node = new_node

        # The new node is now the tail
        self.tail = new_node

        self.length += 1

    def extend(self, collection: collections.abc.Iterable) -> None:
        """
        Take every value in collection, create a new Node, and append it to
        this list
        """

        for value in collection:
            self.append(value)

    def __len__(self) -> int:
        return self.length

    def __iter__(self) -> LinkedList.Iterator:
        second_node = self.head.next_node
        return LinkedList.Iterator(starting_node=second_node)

    def __eq__(self, rhs: LinkedList) -> bool:
        """
        Compare two LinkedList objects for equality based on the elements in
        each list. The two lists must:

            1. Have the same number of elements
            2. Contain identical elements
            3. Contain the identical elements in the same order
        """

        if not isinstance(rhs, LinkedList):
            return False

        if len(self) != len(rhs):
            return False

        return all(lhs_datum == rhs_datum for lhs_datum, rhs_datum in zip(self, rhs))

    def __deepcopy__(self, memo) -> LinkedList:
        list_copy = LinkedList()
        for entry in self:
            list_copy.append(copy.deepcopy(entry))

        return list_copy

    def __add__(self, other: collections.abc.Iterable) -> LinkedList:
        new_ll = LinkedList(self)
        new_ll.extend(other)

        return new_ll

    def __contains__(self, value_to_find: Any) -> bool:
        return any(entry == value_to_find for entry in self)

    def __repr__(self) -> str:
        if not self:
            return "LinkedList()"

        inner_data_str = ", ".join(f"{datum!r}" for datum in self)

        return f"LinkedList(({inner_data_str}))"
