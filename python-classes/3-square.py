#!/usr/bin/python3
"""d."""


class Square:
    """Rn."""

    def __init__(self, size=0):
        """ss"""
        self.size = size  # setter will validate

    @property
    def size(self):
        """Ret"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set th"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return"""
        return self.__size ** 2
