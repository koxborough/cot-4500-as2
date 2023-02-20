import numpy as np

def nevilles_method(x_points, y_points, x):
    matrix = np.zeros((len(x_points), len(x_points)))

    for i in range(len(x_points)):
        matrix[i][0] = y_points[i]

    for i in range(1, len(x_points)):
        for j in range(1, i + 1):
            term_1 = (x - x_points[i - j]) * matrix[i][j - 1]
            term_2 = (x - x_points[i]) * matrix[i - 1][j - 1]
            matrix[i][j] = (term_1 - term_2) / (x_points[i] - x_points[i - j])

    print(matrix[len(x_points) - 1][len(x_points) - 1])

def divided_difference_table(x_points, y_points):
    size = len(x_points)
    matrix = np.zeros((size, size))

    for i in range(size):
        matrix[i][0] = y_points[i]

    for i in range(1, size):
        for j in range(1, i + 1):
            matrix[i][j] = (matrix[i][j - 1] - matrix[i - 1][j - 1]) / (x_points[i] - x_points[i - j])

            if i == j:
                print(matrix[i][j])

    return matrix

def get_approximate_result(matrix, x_points, value, start):
    reoccuring_x_span = 1
    reoccuring_px_result = start
    
    # we only need the diagonals...and that starts at the first row...
    for index in range(1, len(matrix)):
        polynomial_coefficient = matrix[index][index]

        # we use the previous index for x_points....
        reoccuring_x_span *= (value - x_points[index - 1])
        
        # get a_of_x * the x_span
        mult_operation = polynomial_coefficient * reoccuring_x_span

        # add the reoccuring px result
        reoccuring_px_result += mult_operation

    print(reoccuring_px_result)

def hermite_matrix(x_points, y_points, derivative):
    size = 2 * len(x_points)
    matrix = np.zeros((size, size + 1))

    for i in range(size):
        matrix[i][0] = x_points[i // 2]
        matrix[i][1] = y_points[i // 2]

    for i in range(1, size, 2):
        matrix[i][2] = derivative[i // 2]

    for i in range(2, size):
        for j in range(2, i + 2):
            if matrix[i][j] != 0.:
                continue
            
            matrix[i][j] = (matrix[i][j - 1] - matrix[i - 1][j - 1]) / (matrix[i][0] - matrix[i - j + 1][0])

    print(np.matrix(matrix))

# Task One: use Neville's method find 2nd degree interpolating value for f(3.7)
nevilles_method([3.6, 3.8, 3.9], [1.675, 1.436, 1.318], 3.7)
print()

# Task Two: print polynomial approximations for degrees 1, 2, 3
x_points = [7.2, 7.4, 7.5, 7.6]
y_points = [23.5492, 25.3913, 26.8224, 27.4589]
divided_table = divided_difference_table(x_points, y_points)
print()

# Task Three: use the results from Task Two to approximate f(7.3)
get_approximate_result(divided_table, x_points, 7.3, y_points[0])
print()

# Task Four: print Hermite polynomial approximation matrix
hermite_matrix([3.6, 3.8, 3.9], [1.675, 1.436, 1.318], [-1.195, -1.188, -1.182])