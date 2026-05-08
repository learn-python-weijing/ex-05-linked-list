# Exercise 05 — Linked List


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        """Add a new node with value at the END of the list."""
        pass

    def prepend(self, value):
        """Add a new node with value at the BEGINNING of the list."""
        pass

    def delete(self, value):
        """Remove the first node that has the given value.
        If the value is not found, do nothing.
        """
        pass

    def to_list(self):
        """Return all values in the linked list as a Python list.
        Example: if list is 1 -> 2 -> 3, return [1, 2, 3]
        """
        pass

    def length(self):
        """Return the number of nodes in the list."""
        pass

    def contains(self, value):
        """Return True if value exists in the list, False otherwise."""
        pass
