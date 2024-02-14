#!/usr/bin/python3
"""Performs matrix multiplication using the numpy.matmul() function."""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    Parameters:
    m_a (array-like): The first matrix.
    m_b (array-like): The second matrix.

    Returns:
    array-like: The resulting matrix after multiplication.
    """
    return numpy.matmul(m_a, m_b)
