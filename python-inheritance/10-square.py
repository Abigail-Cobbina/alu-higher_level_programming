#!/usr/bin/python3
"""This module defines a square class."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square using a private size."""

    def __init__(self, size):
        """Initialize a square with a validated size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
