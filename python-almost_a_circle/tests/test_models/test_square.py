#!/usr/bin/python3
"""Unit tests for the Square class."""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def test_area(self):
        """Test area calculation."""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_size_type_error(self):
        """Test TypeError for invalid size."""
        with self.assertRaises(TypeError):
            Square("9")

    def test_str(self):
        """Test string representation."""
        s = Square(5, 0, 0, 1)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 5")

    def test_size_getter(self):
        """Test size getter."""
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_size_setter(self):
        """Test size setter."""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.size, 10)


if __name__ == "__main__":
    unittest.main()
