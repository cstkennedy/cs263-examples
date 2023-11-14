import numpy as np


def print_matrices(matrix_XTX, matrix_XTY):
    """
    Print the XTX and XTY matrices
    """

    print("{:*^40}".format("XTX"))
    print(matrix_XTX)

    print()
    print("{:*^40}".format("XTY"))
    print(matrix_XTY)


def find_largest_row_by_col(matrix, col_index):
    num_rows, _ = matrix.shape

    i = col_index
    largest_idx = i
    current_col = i
    for j in range(i + 1, num_rows):
        if matrix[largest_idx, i] < matrix[j, current_col]:
            largest_idx = j

    return largest_idx


def swap_rows(matrix_XTX, matrix_XTY, largest_idx, i):
    if largest_idx != i:
        matrix_XTX[[i, largest_idx], :] = matrix_XTX[[largest_idx, i], :]
        matrix_XTY[[i, largest_idx]] = matrix_XTY[[largest_idx, i]]


def _backsolve(matrix_XTX, matrix_XTY):
    num_rows, _ = matrix_XTX.shape

    for i in reversed(range(1, num_rows)):
        for j in reversed(range(0, i)):
            s = matrix_XTX[j, i]

            matrix_XTX[j, i] -= s * matrix_XTX[i, i]
            matrix_XTY[j] -= s * matrix_XTY[i]


def scale_row(matrix_XTX, matrix_XTY, i):
    scaling_factor = matrix_XTX[i, i]
    matrix_XTX[i, :] /= scaling_factor
    matrix_XTY[i] /= scaling_factor


def eliminate(matrix_XTX, matrix_XTY, i):
    num_rows, _ = matrix_XTX.shape

    for row_i in range(i + 1, num_rows):
        s = matrix_XTX[row_i][i]

        matrix_XTX[row_i] = matrix_XTX[row_i] - s * matrix_XTX[i]
        matrix_XTY[row_i] = matrix_XTY[row_i] - s * matrix_XTY[i]


def solve_matrix(matrix_XTX, matrix_XTY):
    """
    Solve a matrix and return the resulting solution vector
    """

    # Get the dimensions (shape) of the XTX matrix
    num_rows, num_columns = matrix_XTX.shape

    for i in range(0, num_rows):
        # Find column with largest entry
        largest_idx = find_largest_row_by_col(matrix_XTX, i)

        # Swap
        current_col = i
        swap_rows(matrix_XTX, matrix_XTY, largest_idx, current_col)

        # Scale
        scale_row(matrix_XTX, matrix_XTY, i)

        # Eliminate
        eliminate(matrix_XTX, matrix_XTY, i)

    _backsolve(matrix_XTX, matrix_XTY)

    return matrix_XTY


def main():
    points = [(0.0, 0.0), (1.0, 1.0), (2.0, 4.0)]

    # Compute X
    x_values = [x for x, _ in points]
    x_values = np.array(x_values)
    x_values_squared = x_values ** 2
    matrix_X = np.column_stack((np.ones(len(points)), x_values, x_values_squared))

    # Compute Y
    matrix_Y = np.array([y for _, y in points])

    matrix_XT = matrix_X.transpose()

    # Compute XTX and XTY
    matrix_XTX = np.matmul(matrix_XT, matrix_X)
    matrix_XTY = np.matmul(matrix_XT, matrix_Y)

    print_matrices(matrix_XTX, matrix_XTY)

    matrix_XTY = matrix_XTY.reshape(matrix_XTX.shape[0], 1)
    matrix_augmented = np.hstack((matrix_XTX, matrix_XTY))
    print(matrix_augmented)

    solution = solve_matrix(matrix_augmented)

    print()
    print("{:-^40}".format("Solution"))
    print(np.polynomial.Polynomial(solution))


if __name__ == "__main__":
    main()
