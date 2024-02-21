import numpy as np

def generate_one_diagonal_line(rows, cols):
    matrix = np.zeros((rows, cols), dtype=int)

    # for i in range(min(rows, cols)):
    #     matrix[i, i] = 1

    for j in range(rows):
        for i in range(min(rows, cols)):
            try:
                matrix[i+j, i] = 1
            except IndexError:
                pass

    return matrix


def generate_diagonal_lines(rows, cols, num_lines):
    matrix = np.zeros((rows, cols), dtype=int)

    for _ in range(num_lines):
        # Randomly select a start position along the first row or first column
        start_row = np.random.randint(0, rows)
        start_col = np.random.randint(0, cols)

        # Determine the direction of the line
        direction = np.random.choice(['up', 'down', 'left', 'right'])

        # Fill the matrix with the diagonal line
        if direction == 'up':
            for i in range(min(start_row, cols - start_col)):
                matrix[start_row - i, start_col + i] = 1
        elif direction == 'down':
            for i in range(min(rows - start_row, cols - start_col)):
                matrix[start_row + i, start_col + i] = 1
        elif direction == 'left':
            for i in range(min(start_col, rows - start_row)):
                matrix[start_row + i, start_col - i] = 1
        elif direction == 'right':
            for i in range(min(cols - start_col, rows - start_row)):
                matrix[start_row + i, start_col + i] = 1

    return matrix


def gen_horizontal_lines(rows, cols, color: int):
    matrix = np.zeros((rows, cols), dtype=int)

    # Generate horizontal lines in between each row
    for i in range(1, rows, 2):
        matrix[i, :] = color

    return matrix

def gen_vertical_lines(rows, cols, color):
    matrix = np.zeros((rows, cols), dtype=int)

    # Generate vertical lines in between each column
    for j in range(1, cols, 2):
        matrix[:, j] = color

    return matrix


def gen_noisy_matrix(rows, cols, noise_level, color: int):
    matrix = np.zeros((rows, cols), dtype=int)  # Generate a random binary matrix

    # Inject random noise
    for i in range(rows):
        for j in range(cols):
            if sum(np.random.binomial(9, 0.01, 20) == 1)/20 < noise_level:
                matrix[i, j] = color  # Flip the value randomly

    return matrix

def gen_square_background(rows, cols, color):
    matrix = np.zeros((rows, cols), dtype=int)
    row = col = np.random.randint(rows * 0.7, rows)
    matrix[1:row, 1:col] = color
    return matrix


# Example usage:
rows = 10
cols = 10
noise_level = 0.0001  # Adjust the noise level as desired
noisy_matrix = generate_noisy_matrix(rows, cols, noise_level, 2)
print(noisy_matrix)