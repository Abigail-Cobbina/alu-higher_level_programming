#!/usr/bin/python3
"""Unit tests for the Rectangle class."""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def test_area(self):
        """Test area calculation."""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_width_type_error(self):
        """Test TypeError for invalid width."""
        with self.assertRaises(TypeError):
            Rectangle("10", 2)

    def test_height_value_error(self):
        """Test ValueError for invalid height."""
        with self.assertRaises(ValueError):
            Rectangle(10, -2)

    def test_x_type_error(self):
        """Test TypeError for invalid x."""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, {})

    def test_y_value_error(self):
        """Test ValueError for invalid y."""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)

    def test_str(self):
        """Test string representation."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")


if __name__ == "__main__":
    unittest.main()
