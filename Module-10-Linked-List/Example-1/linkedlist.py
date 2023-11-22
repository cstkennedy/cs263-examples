from __future__ import annotations

from dataclasses import dataclass
from typing import Any


class LinkedList:
    @dataclass
    class Node:
        data: Any = None
        next_node: Node = None

    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self.length: int = 0

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

    def __len__(self) -> int:
        return self.length

    def __str__(self) -> str:
        """
        Iterate through the LinkedList and print each individual Node
        with an index.
        """

        output_str = ""
        idx = 0

        it = self.head

        while it:
            output_str += f"Node #{idx:} contains {it.data}\n"

            it = it.next_node
            idx += 1

        return output_str
