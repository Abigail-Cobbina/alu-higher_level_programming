#!/usr/bin/python3
"""This module checks if an object is exactly an instance of a class."""


def is_same_class(obj, a_class):
    """Return True if an object is exactly an instance of a class."""
    return type(obj) is a_class
