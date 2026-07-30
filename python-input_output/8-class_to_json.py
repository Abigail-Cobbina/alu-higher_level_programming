#!/usr/bin/python3
"""This module returns a dictionary representation of an object."""


def class_to_json(obj):
    """Return the dictionary description of an object."""
    return obj.__dict__
