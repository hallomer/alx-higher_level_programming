#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        for i, element in enumerate(list):
            print("{}".format(element), end="")
            if i < len(list) - 1:
                print(" ", end="")
        print()
