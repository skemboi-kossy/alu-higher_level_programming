#!/usr/bin/python3
"""Module that defines a Square class with a size property."""


class Square:
    """Represents a square with a controlled, validated size attribute."""

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

    @property
    def size(self):
        """Retrieve the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set a new size for the square, validating the value.

        Args:
            value: the new size to assign.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size
