#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = list(a_dictionary.keys())
    for k in keys:
        if value == a_dictionary.get(k):
            del a_dictionary[k]
    return a_dictionary
