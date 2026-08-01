#!/usr/bin/python3
"""Unit tests for the Base class."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def test_id_auto(self):
        """Test auto-assigned id."""
        Base._Base__nb_objects = 0
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_id_given(self):
        """Test manually assigned id."""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_to_json_string_empty(self):
        """Test to_json_string with empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_none(self):
        """Test to_json_string with None."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_from_json_string_empty(self):
        """Test from_json_string with empty string."""
        self.assertEqual(Base.from_json_string("[]"), [])


if __name__ == "__main__":
    unittest.main()
