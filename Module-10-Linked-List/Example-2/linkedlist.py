from __future__ import annotations

import copy
import collections.abc
from dataclasses import dataclass
from typing import Any


class LinkedList(collections.abc.Iterable):
    @dataclass
    class Node:
        data: Any = None
        next_node: Node = None

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
        self.head: Node = None
        self.tail: Node = None
        self.length: int = 0

        # Use extend to add any starting data
        if initial_data:
            self.extend(initial_data)

    def __append_first(self, val):
        """
        Add the very first node
        """

        new_node = LinkedList.Node(val)

        self.head = new_node
        self.tail = new_node

        self.length = 1

    def __append_general(self, val):
        """
        Add every node other than the first node
        """

        new_node = LinkedList.Node(val)

        # Add the new node after the current tail
        self.tail.next_node = new_node

        # The new node is now the tail
        self.tail = new_node

        self.length += 1

    def append(self, val: Any) -> None:
        """
        Add a piece of data (entry) to the end of the list. If the list is
        currently empty, this new entry will be both the first and last entry
        in the list.

        Args:
            val: piece of data to store
        """

        if not self.head:
            self.__append_first(val)

        else:
            self.__append_general(val)

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
        return LinkedList.Iterator(starting_node=self.head)

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

    def __repr__(self) -> str:
        inner_data_str = ", ".join(f"{datum!r}" for datum in self)

        return f"LinkedList(({inner_data_str}))"

    def __str__(self) -> str:
        """
        Iterate through the LinkedList and print each individual Node
        with an index.
        """

        return "\n".join(
            f"Node #{idx:} contains {data}" for idx, data in enumerate(self)
        )
