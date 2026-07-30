#!/usr/bin/python3
"""This module checks if an object belongs to a class or its subclasses."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or its subclass."""
    return isinstance(obj, a_class)
