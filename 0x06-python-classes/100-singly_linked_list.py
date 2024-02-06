#!/usr/bin/python3

"""Represents a node in a singly linked list."""


class Node:
    """
    Attributes:
        _data: The data stored in the node.
        _next_node: The reference to the next node.

    Methods:
        __init__(data, next_node=None):
               Initializes a new instance of the Node class.
        data(): Getter method for the data attribute.
        data(value): Setter method for the data attribute.
        next_node(): Getter method for the next_node attribute.
        next_node(value): Setter method for the next_node attribute.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new instance of the Node class.

        Args:
            data: The data to be stored in the node.
            next_node: The reference to the next node. Defaults to None.
        """
        self._data = None
        self._next_node = None
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter method for the data attribute."""
        return self._data

    @data.setter
    def data(self, value):
        """Setter method for the data attribute."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """Getter method for the next_node attribute."""
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """Setter method for the next_node attribute."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object or None")
        self._next_node = value


"""Represents a singly linked list."""


class SinglyLinkedList:
    """
    Attributes:
        head: The head node of the linked list.

    Methods:
        __init__(): Initializes a new instance of the SinglyLinkedList class.
        sorted_insert(value):
              Inserts a value into the linked list in sorted order.
        __str__(): Returns a string representation of the linked list.
    """

    def __init__(self):
        """Initializes a new instance of the SinglyLinkedList class."""
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a value into the linked list in sorted order.

        Args:
            value: The value to be inserted.
        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.
        """
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.rstrip()
