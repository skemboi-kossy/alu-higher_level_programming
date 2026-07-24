#!/usr/bin/python3
"""Module that defines a Square class with an area method."""


class Square:
    """Represents a square that can compute its own area."""

    def __init__(self, size=0):
        """Initialize a new Square, validating the size argument.

        Args:
            size: the length of one side of the square, defaults to 0.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size
