#!/usr/bin/python3
""" Divides each element of a matrix by a given number."""


def matrix_divided(matrix, div):
    """
    Parameters:
    matrix (list of lists): The matrix to be divided.
    Each element must be an integer or a float.
    div (int or float): The number to divide each element of the matrix by.

    Raises:
    TypeError: If `matrix` is not a list of lists,
    or if any element of the matrix is not an integer or a float.
    TypeError: If the rows of the matrix have different sizes.
    TypeError: If `div` is not a number.
    ZeroDivisionError: If `div` is zero.

    Returns:
    list of lists: The resulting matrix,
    where each element is the result of dividing the corresponding element
    of the original matrix by `div`, rounded to 2 decimal places.
    """
    if not isinstance(matrix, list) or any(
       not isinstance(i, list) for i in matrix):
        raise TypeError("matrix must be a matrix\
                        (list of lists) of integers/floats")
    size = -1
    for row in matrix:
        if size == -1:
            size = len(row)
        elif size != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if type(element) is not int and type(element) is not float:
                raise TypeError("matrix must be a matrix \
                                (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    matrix2 = [[round(element/div, 2) for element in row] for row in matrix]
    return matrix2
