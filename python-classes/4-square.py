#!/usr/bin/python3
"""Module tha method."""


class Square:
    """Represation."""

    def __init__(self, size=0):
        """In size."""
        self.size = size  # setter will validate

    @property
    def size(self):
        """Rere."""
        return self.__size

    @size.setter
    def size(self, value):
        """idation."""
        if not isinstance(value, int):

