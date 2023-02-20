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

# Task One: use Neville's method find 2nd degree interpolating value for f(3.7)
nevilles_method([3.6, 3.8, 3.9], [1.675, 1.436, 1.318], 3.7)