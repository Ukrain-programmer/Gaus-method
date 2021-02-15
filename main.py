#!/usr/bin/env python3
import math

def get_transform_to_f3(num, digits ):
    param = '%.' + str(digits) + 'f'
    num = float(param % num)
    return num

def get_determinant(matrix):
    return matrix[0][0]*matrix[1][1]*matrix[2][2] + matrix[0][1] * matrix[1][2] * matrix[2][0] + matrix[0][2] * matrix[1][0] * \
           matrix[2][1] - matrix[0][0] * matrix[1][2] * matrix[2][1] - matrix[0][1] * matrix[1][0] * matrix[2][2] - matrix[0][2]*matrix[1][1]* matrix[2][0]

def print_matrix (matrix):
    for i in matrix:
        for j in i:
            print(j, end='\t\t')
        print()

def del_minus_zero(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == -0:
                matrix[i][j] = abs(matrix[i][j])
    return matrix

def process(matrix):
    if get_determinant(matrix) == 0:
        return "Determ is 0"
    first_div = matrix[0][0]
    second_div = matrix[1][0]
    third_div = matrix[2][0]

    for i in range(len(matrix[0])):
        matrix[0][i] /= first_div
        matrix[1][i] -= matrix[0][i]*second_div
        matrix[2][i] -= matrix[0][i]*third_div
    fourth_div = matrix[1][1]
    fifth_div = matrix[0][1]
    sixth_div = matrix[2][1]

    for i in range(len(matrix[0])):
        matrix[1][i] /= fourth_div
        matrix[0][i] -= matrix[1][i] * fifth_div
        matrix[2][i] -= matrix[1][i] * sixth_div

    seventh = matrix[2][2]
    eight_div = matrix[0][2]
    nineth_div = matrix[1][2]
    for i in range(len(matrix[0])):
        matrix[2][i] /= seventh
        matrix[0][i] -= matrix[2][i] * eight_div
        matrix[1][i] -= matrix[2][i] * nineth_div

    matrix[0][3] = get_transform_to_f3(matrix[0][3], 2)
    matrix[1][3] = get_transform_to_f3(matrix[1][3], 2)
    matrix[2][3] = get_transform_to_f3(matrix[2][3], 2)

    matrix = del_minus_zero(matrix)
    return matrix

if __name__ == '__main__':
    matrix = []

    print("Enter row use split ,")
    for i in range(3):
        first = input().split(",")
        first = [float(i) for i in first]
        matrix.append(list(first))

    print_matrix(process(matrix))
