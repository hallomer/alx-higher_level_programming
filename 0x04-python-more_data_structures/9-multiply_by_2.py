#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    multiplied = {key: value * 2 for key, value in new_dict.items()}
    return multiplied
