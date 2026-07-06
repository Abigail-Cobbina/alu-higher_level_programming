#!/usr/bin/python3
"""Module that defines a function to check divisibility by 2."""


def divisible_by_2(my_list=[]):
    """Return a list of booleans indicating divisibility by 2.

    Args:
        my_list (list): list of integers.

    Returns:
        list: list of True/False values, same size as my_list.
    """
    result = []
    for number in my_list:
        result.append(number % 2 == 0)
    return result
