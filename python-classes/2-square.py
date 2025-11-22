#!/usr/bin/python3
"""asa"""


def __init__(self, size=0):
    """ss"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    self.__size = size
    def area(self):
        return self._size ** 2
