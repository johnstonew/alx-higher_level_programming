#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    def modify_list(lVals):
        return [x if not isinstance(x, list) else x[:] for x in lVals]
    new_matrix = modify_list(matrix)
    for rows in range(len(new_matrix)):
        for num in range(len(new_matrix[rows])):
            new_matrix[rows][num] *= new_matrix[rows][num]
    return new_matrix
