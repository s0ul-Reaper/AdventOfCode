import numpy as np
with open('input.txt', 'r') as f:
    input = [line.replace('\n', '').replace('move ', '').replace(
        ' from ', ',').replace(' to ', ',').split(',') for line in f][10::]

# input.txt, [10::]


def str_to_int(x: str) -> list:
    return [int(i) for i in x]


des = [str_to_int(i) for i in input]

temp = [str_to_int(i) for i in input]

for i in temp:
    i[1] = i[1]-1
data = temp

# # Matix initialization

matrix = np.empty((56, 9), dtype=str)


def init():

    matrix[48][1], matrix[48][4], matrix[48][6] = 'W', 'J', 'J'
    matrix[49][1], matrix[49][3], matrix[49][4], matrix[49][5], matrix[49][6] = 'V', 'F', 'F', 'S', 'S'
    matrix[50][1], matrix[50][2], matrix[50][3], matrix[50][4], matrix[50][5], matrix[50][6] = 'S', 'M', 'R', 'W', 'M', 'C'
    matrix[51][1], matrix[51][2], matrix[51][3], matrix[51][4], matrix[51][5], matrix[51][6], matrix[51][8] = 'M', 'G', 'W', 'S', 'F', 'G', 'C'
    matrix[52][0], matrix[52][1], matrix[52][2], matrix[52][3], matrix[52][4], matrix[
        52][5], matrix[52][6], matrix[52][8] = 'W', 'P', 'S', 'M', 'H', 'N', 'F', 'L'
    matrix[53][0], matrix[53][1], matrix[53][2], matrix[53][3], matrix[53][4], matrix[53][5], matrix[
        53][6], matrix[53][7], matrix[53][8] = 'R', 'H', 'T', 'D', 'L', 'D', 'D', 'B', 'W'
    matrix[54][0], matrix[54][1], matrix[54][2], matrix[54][3], matrix[54][4], matrix[54][5], matrix[
        54][6], matrix[54][7], matrix[54][8] = 'T', 'C', 'L', 'H', 'Q', 'J', 'B', 'T', 'N'
    matrix[55][0], matrix[55][1], matrix[55][2], matrix[55][3], matrix[55][4], matrix[55][5], matrix[
        55][6], matrix[55][7], matrix[55][8] = 'G', 'G', 'C', 'J', 'P', 'P', 'Z', 'R', 'H'
    return matrix


# matrix = np.empty((6, 3), dtype=str)

# matrix[5][0], matrix[5][1], matrix[5][2] = 'Z', 'M', 'P'
# matrix[4][0], matrix[4][1] = 'N', 'C'
# matrix[3][1] = 'D'


def hill_point(matrix: np.ndarray, column: int) -> str:
    iceberg_hill = ''
    exact_point = [0 for x in range(2)]
    for i in range(matrix.shape[0]):
        if matrix[i][column] != '':
            iceberg_hill += matrix[i][column]
            exact_point[0] = i
            exact_point[1] = column
            return [iceberg_hill, exact_point]


def destination(matrix: np.ndarray, x: list) -> list:
    for i in range(matrix.shape[0]):
        if i == matrix.shape[0]-1 and matrix[i][x[2]-1] == '':
            return [i, x[2]-1]
        if matrix[i][x[2]-1] != '':
            return ([i-1, x[2]-1])


def result(matrix):
    temp = []
    for i in range(matrix.shape[1]):
        temp.append(hill_point(matrix, i)[0])
    return ''.join(temp)


# Part A
def old_constructor():
    init()
    for y in range(len(data)):
        for i in range(data[y][0]):
            matrix[destination(matrix, des[y])[0]][destination(matrix, des[y])
                                                   [1]] = hill_point(matrix, data[y][1])[0]
            matrix[hill_point(matrix, data[y][1])[1][0]][hill_point(
                matrix, data[y][1])[1][1]] = ''
    return result(matrix)


# Part b
def new_constructor():
    init()
    for y in range(len(data)):
        reverse_from = hill_point(matrix, data[y][1])[1][0]
        reverse_to = hill_point(matrix, data[y][1])[1][0] + data[y][0]
        reversed_subarray = np.flip(
            matrix[reverse_from:reverse_to, data[y][1]], axis=0)
        matrix[reverse_from:reverse_to, data[y][1]] = reversed_subarray
        for i in range(data[y][0]):
            matrix[destination(matrix, des[y])[0]][destination(matrix, des[y])
                                                   [1]] = hill_point(matrix, data[y][1])[0]
            matrix[hill_point(matrix, data[y][1])[1][0]][hill_point(
                matrix, data[y][1])[1][1]] = ''
    return result(matrix)


print(
    f'The solution of part a is: {old_constructor()}\nThe solution of part b is {new_constructor()}')
