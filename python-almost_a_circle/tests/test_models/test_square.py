#!/usr/bin/python3
"""Unit tests for the Square class."""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def test_square_1_2(self):
        """Test Square(1, 2)."""
        s = Square(1, 2)
        self.assertEqual(s.x, 2)

    def test_square_1_2_3(self):
        """Test Square(1, 2, 3)."""
        s = Square(1, 2, 3)
        self.assertEqual(s.y, 3)

    def test_square_str_x(self):
        """Test Square(1, '2') raises TypeError."""
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_square_str_y(self):
        """Test Square(1, 2, '3') raises TypeError."""
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_square_neg(self):
        """Test Square(-1) raises ValueError."""
        with self.assertRaises(ValueError):
            Square(-1)

    def test_square_neg_x(self):
        """Test Square(1, -2) raises ValueError."""
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_square_neg_y(self):
        """Test Square(1, 2, -3) raises ValueError."""
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_square_zero(self):
        """Test Square(0) raises ValueError."""
        with self.assertRaises(ValueError):
            Square(0)

    def test_area(self):
        """Test area calculation."""
        s = Square(5)
        self.assertEqual(s.area(), 25)

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

    def test_to_dictionary(self):
        """Test to_dictionary method."""
        s = Square(10, 2, 1)
        d = s.to_dictionary()
        self.assertEqual(d['size'], 10)
        self.assertEqual(d['x'], 2)
        self.assertEqual(d['y'], 1)

    def test_update_no_args(self):
        """Test update with no args."""
        s = Square(1)
        s.update()
        self.assertEqual(s.size, 1)

    def test_update_89(self):
        """Test update(89)."""
        s = Square(1)
        s.update(89)
        self.assertEqual(s.id, 89)

    def test_update_89_1(self):
        """Test update(89, 1)."""
        s = Square(1)
        s.update(89, 1)
        self.assertEqual(s.size, 1)

    def test_update_89_1_2(self):
        """Test update(89, 1, 2)."""
        s = Square(1)
        s.update(89, 1, 2)
        self.assertEqual(s.x, 2)

    def test_update_89_1_2_3(self):
        """Test update(89, 1, 2, 3)."""
        s = Square(1)
        s.update(89, 1, 2, 3)
        self.assertEqual(s.y, 3)

    def test_update_kwargs_id(self):
        """Test update(**{'id': 89})."""
        s = Square(1)
        s.update(**{'id': 89})
        self.assertEqual(s.id, 89)

    def test_update_kwargs_id_size(self):
        """Test update(**{'id': 89, 'size': 1})."""
        s = Square(1)
        s.update(**{'id': 89, 'size': 1})
        self.assertEqual(s.size, 1)

    def test_update_kwargs_id_size_x(self):
        """Test update(**{'id': 89, 'size': 1, 'x': 2})."""
        s = Square(1)
        s.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.x, 2)

    def test_update_kwargs_all(self):
        """Test update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})."""
        s = Square(1)
        s.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.y, 3)

    def test_create_id(self):
        """Test Square.create(**{'id': 89})."""
        s = Square.create(**{'id': 89})
        self.assertEqual(s.id, 89)

    def test_create_id_size(self):
        """Test Square.create(**{'id': 89, 'size': 1})."""
        s = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(s.size, 1)

    def test_create_id_size_x(self):
        """Test Square.create(**{'id': 89, 'size': 1, 'x': 2})."""
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.x, 2)

    def test_create_all(self):
        """Test Square.create with all attributes."""
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.y, 3)

    def test_save_to_file_none(self):
        """Test Square.save_to_file(None)."""
        import os
        Square.save_to_file(None)
        self.assertTrue(os.path.exists("Square.json"))

    def test_save_to_file_empty(self):
        """Test Square.save_to_file([])."""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_one(self):
        """Test Square.save_to_file([Square(1)])."""
        import os
        Square.save_to_file([Square(1)])
        self.assertTrue(os.path.exists("Square.json"))

    def test_load_from_file_no_file(self):
        """Test Square.load_from_file() when file doesn't exist."""
        import os
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_exists(self):
        """Test Square.load_from_file() when file exists."""
        Square.save_to_file([Square(1)])
        result = Square.load_from_file()
        self.assertEqual(len(result), 1)

def test_square_str_size(self):
        """Test Square('1') raises TypeError."""
        with self.assertRaises(TypeError):
            Square("1")

    def test_save_to_file_none_exists(self):
        """Test Square.save_to_file(None) creates file."""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_square(self):
        """Test Square.save_to_file([Square(1)])."""
        Square.save_to_file([Square(1)])
        with open("Square.json", "r") as f:
            content = f.read()
        self.assertIn("size", content)

if __name__ == "__main__":
    unittest.main()
