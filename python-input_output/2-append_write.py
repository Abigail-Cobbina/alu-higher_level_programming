#!/usr/bin/python3
"""This module appends strings to UTF8 text files."""


def append_write(filename="", text=""):
    """Append text to a file and return the number of characters added."""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
