#!/usr/bin/python3
"""This module contains a function to read and display text files."""


def read_file(filename=""):
    """Read a UTF8 text file and print its contents to stdout."""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
