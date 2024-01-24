#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    else:
        roman_number = 0
        for i in roman_string:
            if i == "I":
                roman_number += 1
            elif i == "V":
                roman_number += 5
            elif i == "X":
                roman_number += 10
            elif i == "L":
                roman_number += 50
            elif i == "C":
                roman_number += 100
            elif i == "D":
                roman_number += 500
            elif i == "M":
                roman_number += 1000
    return int(roman_number)
