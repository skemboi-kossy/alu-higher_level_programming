#!/usr/bin/python3
"""Module that defines a Square class with a private size attribute."""


class Square:
    """Represents a square defined by a private instance attribute."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size: the length of one side of the square.
        """
        self.__size = size
