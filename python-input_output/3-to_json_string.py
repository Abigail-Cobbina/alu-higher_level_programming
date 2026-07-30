#!/usr/bin/python3
"""This module converts Python objects into JSON strings."""

import json


def to_json_string(my_obj):
    """Return the JSON representation of an object."""
    return json.dumps(my_obj)
