class Point3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z


def matmul1(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Number of columns in the first matrix must equal the number of rows in the second matrix")
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result


def matmul2(matrix1, point3D):
    return matmul1(matrix1, vecToMatrix(point3D))


def vecToMatrix(point_3d):
    return [[point_3d.x], [point_3d.y], [point_3d.z]]


def matrixToVec(matrix):
    num1, num1.x, num1.y = Point3D(), matrix[0][0], matrix[1][0]
    if len(matrix) > 2:
        num1.z = matrix[2][0]
    return num1


def multiply_matrix_by_scalar(matrix, scalar):
    rows, cols, result_matrix = len(matrix), len(matrix[0]), []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix[i][j] * scalar)
        result_matrix.append(row)
    return result_matrix
