#!/usr/bin/python3
""" module that divides all integers of a matric
Args:
matrix (list): A matrix
div (int): Number to divide matrix
"""


def matrix_divided(matrix, div):
    """ Function that divides all elements of a matrix
    Returns a new matrix
    """

    text = "matrix must be a matrix (list of lists) of integers/floats"
    my_matrix = []
    if not matrix or matrix is [[]] or matrix is None:
        raise TypeError(text)
    if type(div) == int or type(div) == float or div is None:
        pass  # improper div value type checks
    else:
        raise TypeError("div must be a number")
    if div == 0:  # if div is zero
        raise ZeroDivisionError("division by zero")
    if matrix[0]:  # if matrix is empty or not
        length = len(matrix[0])
    else:
        raise TypeError(text)
    for i in range(len(matrix)):  # real work. the appending
        if len(matrix[i]) is not length:
            raise TypeError("Each row of the matrix must have the same size")
        my_matrix.append([])
        for b in matrix[i]:
            if type(b) is int or type(b) is float:
                my_matrix[i].append(round(b / div, 2))
            else:
                raise TypeError(text)
    return my_matrix
