#!/usr/bin/python3
"""Performs matrix multiplication on two matrices."""


def matrix_mul(m_a, m_b):
    """
    Parameters:
    m_a (list): The first matrix.
    m_b (list): The second matrix.

    Raises:
    TypeError: If `m_a` is not a list or if any element in `m_a` is not a list.
    TypeError: If `m_b` is not a list or if any element in `m_b` is not a list.
    TypeError: If any element in `m_a` is not an integer or a float.
    TypeError: If any element in `m_b` is not an integer or a float.
    ValueError: If `m_a` is empty or contains an empty row.
    ValueError: If `m_b` is empty or contains an empty row.
    TypeError: If any row in `m_a` has a different length.
    TypeError: If any row in `m_b` has a different length.
    ValueError: If the number of columns in `m_a` is
    not equal to the number of rows in `m_b`.

    Returns:
    list: The resulting matrix after multiplication.
    """
    # Type and shape checks
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    m_a_empty = False
    m_b_empty = False
    m_a_notrect = False
    m_b_notrect = False
    m_a_notnum = False
    m_b_notnum = False

    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        if len(row) != len(m_a[0]):
            m_a_notrect = True
        for num in row:
            if not isinstance(num, (int, float)):
                m_a_notnum = True

    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
        if len(row) != len(m_b[0]):
            m_b_notrect = True
        for num in row:
            if not isinstance(num, (int, float)):
                m_b_notnum = True

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    if m_a_notnum:
        raise TypeError("m_a should contain only integers or floats")

    if m_b_notnum:
        raise TypeError("m_b should contain only integers or floats")

    if m_a_notrect:
        raise TypeError("each row of m_a must should be of the same size")

    if m_b_notrect:
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Matrix multiplication
    res = [[] for i in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            c = 0
            for k in range(len(m_b)):
                c += m_a[i][k] * m_b[k][j]
            res[i].append(c)

    return res


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")
