import numpy as np


def swap_current_row_with_largest_row(matrix: np.array, current_idx: int) -> None:
    """
    Find the row (starting with the current row) with the largest entry in the
    column with the same index as the current row (e.g., matrix[1,1]). Consider
    only rows below the current one.

    Args:
        matrix: augmented matrix to update

        current_idx: current row (and column) index
    """

    num_rows, _ = matrix.shape

    # Find the row with the largest column entry
    row_idx = current_idx
    largest_idx = row_idx
    current_col = current_idx
    for j in range(row_idx + 1, num_rows):
        if matrix[largest_idx, row_idx] < matrix[j, current_col]:
            largest_idx = j

    # If the current row is not the largest row then swap
    if largest_idx != current_idx:
        matrix[[current_idx, largest_idx], :] = matrix[[largest_idx, current_idx], :]


def _backsolve(matrix: np.array) -> None:
    """
    Back solve the matrix by performing the necessary row scale and subtraction
    operations to obtain a diagonal matrix with ones on the diagonal.

    The augmented column will contain the solution.

    Args:
        matrix: augmented matrix
    """
    num_rows, _ = matrix.shape

    for i in reversed(range(1, num_rows)):
        for j in reversed(range(0, i)):
            scaling_factor = matrix[j, i]

            matrix[j, [i, -1]] -= scaling_factor * matrix[i, [i, -1]]


def scale_row(matrix: np.array, current_row_idx: int) -> None:
    """
    Scale every entry of the current row by the value of the corresponding
    column (e.g., matrix[2,2])
    """

    scaling_factor = matrix[current_row_idx, current_row_idx]
    matrix[current_row_idx, :] /= scaling_factor


def eliminate(matrix: np.array, current_row_idx: int) -> None:
    """
    Subract multiples of the current rows from all rows below it. Once this
    function completes all rows below this one will contain zero in the
    "current_row_idx" column
    """

    num_rows, _ = matrix.shape

    for row_i in range(current_row_idx + 1, num_rows):
        scaling_factor = matrix[row_i][current_row_idx]

        matrix[row_i] = matrix[row_i] - scaling_factor * matrix[current_row_idx]


def solve_matrix(matrix_augmented: np.array) -> np.array:
    """
    Solve a matrix and return the resulting solution vector

    Args:
        matrix_augmented: an n-by-n matrix with a vector augmented in the
        right-most column

    Returns:
        constants c_0, c_1, c_2, ... c_n depending on the number of rows in the
        supplied matrix
    """

    # Get the number of rows in the matrix
    num_rows, _ = matrix_augmented.shape

    for current_row_idx in range(0, num_rows):
        swap_current_row_with_largest_row(matrix_augmented, current_row_idx)
        scale_row(matrix_augmented, current_row_idx)
        eliminate(matrix_augmented, current_row_idx)

    _backsolve(matrix_augmented)

    return matrix_augmented[:, -1].flatten()


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

    matrix_XTY = matrix_XTY.reshape(matrix_XTX.shape[0], 1)
    matrix_augmented = np.hstack((matrix_XTX, matrix_XTY))

    print("{:*^40}".format("XTX"))
    print(matrix_XTX)

    print()
    print("{:*^40}".format("XTY"))
    print(matrix_XTY)

    print()
    print("{:*^40}".format("XTX|XTY"))
    print(matrix_augmented)

    solution = solve_matrix(matrix_augmented)

    print()
    print("{:-^40}".format("Solution"))
    print(np.polynomial.Polynomial(solution))


if __name__ == "__main__":
    main()
