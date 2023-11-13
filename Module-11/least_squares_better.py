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


def _backsolve(matrix_augmented):

    num_rows, _ = matrix_augmented.shape

    for i in reversed(range(1, num_rows)):
        for j in reversed(range(0, i)):
            s = matrix_augmented[j, i]

            matrix_augmented[j, [i, -1]] -= (s * matrix_augmented[i, [i,-1]])


def solve_matrix(matrix_augmented):
    """
    Solve a matrix and return the resulting solution vector
    """

    # Get the dimensions (shape) of the XTX matrix
    num_rows, _ = matrix_augmented.shape

    for i in range(0, num_rows):
        # Find column with largest entry and swap
        largest_idx = i + np.argmax(matrix_augmented[i:, :], axis=0)[i]

        if largest_idx != i:
            matrix_augmented[[i, largest_idx], :] = matrix_augmented[[largest_idx, i], :]

        # Scale
        scaling_factor = np.reciprocal(matrix_augmented[i, i])
        matrix_augmented[i, :] *= scaling_factor

        # Eliminate
        for row_i in range(i + 1, num_rows):
            s = matrix_augmented[row_i][i]

            matrix_augmented[row_i] = matrix_augmented[row_i] - s * matrix_augmented[i]

    _backsolve(matrix_augmented)

    return matrix_augmented[:, -1].flatten()


def main():

    # Set up input data points, X, Y, and XT
    points = [(0., 0.), (1., 1.), (2., 4.)]

    matrix_X = np.array([[1., 0., 0.],
                         [1., 1., 1.],
                         [1., 2., 4.]])

    matrix_Y = np.array([0, 1, 4])

    matrix_XT = matrix_X.transpose()

    # Compute XTX and XTY
    matrix_XTX = np.matmul(matrix_XT, matrix_X)
    matrix_XTY = np.matmul(matrix_XT, matrix_Y)

    print_matrices(matrix_XTX, matrix_XTY)
    matrix_augmented = np.hstack((matrix_XTX, matrix_XTY.reshape(matrix_XTX.shape[0], 1)))
    print(matrix_augmented)

    print()
    print("{:-^40}".format("Solution"))
    solution = solve_matrix(matrix_augmented)
    print(solution)
    print(np.polynomial.Polynomial(solution))


if __name__ == "__main__":
    main()
