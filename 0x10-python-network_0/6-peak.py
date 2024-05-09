#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Finds a peak."""
    if not list_of_integers or list_of_integers == []:
        return None
    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
