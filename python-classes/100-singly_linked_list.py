#!/usr/bin/python3
"""Module for singly linked list"""


class Node:
    """Defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initialize a new Node

        Args:
            data: integer value for the node
            next_node: next node in the list (default None)
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data attribute"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data attribute

        Args:
            value: must be an integer

        Raises:
            TypeError: if value is not an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next_node attribute"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next_node attribute

        Args:
            value: must be None or a Node object

        Raises:
            TypeError: if value is not None or a Node
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list"""

    def __init__(self):
        """Initialize an empty singly linked list"""
        self.__head = None

    def __str__(self):
        """Return string representation of the list"""
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position

        Args:
            value: integer value for the new node
        """
        new_node = Node(value)

        # Case 1: Empty list or new value is smaller than head
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        # Case 2: Find the position to insert
        current = self.__head
        while current.next_node and current.next_node.data < value:
            current = current.next_node

        # Insert the node
        new_node.next_node = current.next_node
        current.next_node = new_node
