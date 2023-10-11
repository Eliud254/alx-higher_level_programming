#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []

    for row in matrix:
        new_row = []

        for element in row:
            new_row.append(element ** 2)

        new_matrix.append(new_row)

    return new_matrix
