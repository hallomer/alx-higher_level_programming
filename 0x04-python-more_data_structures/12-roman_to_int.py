#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    else:
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        roman_number = 0
        previous_value = 0
        for i in roman_string:
            if i in roman_values:
                current_value = roman_values[i]
                if current_value > previous_value:
                    roman_number += current_value - 2 * previous_value
                else:
                    roman_number += current_value
                previous_value = current_value
        return roman_number
