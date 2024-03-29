import numpy as np
import math
import random

color_encoding = {
    0: "black",
    1: "blue",
    2: "red",
    3: "green",
    4: "yellow",
    5: "gray",
    6: "magenta",
    7: "orange",
    8: "cyan",
    9: "brown",
}

def generate_random_matrix(rows, cols, num_shapes, shape_size, shape_type):
    matrix = np.zeros((rows, cols), dtype=int)

    for _ in range(num_shapes):
        color = random.choice(colors)
        if shape_type == 'square':
            row = np.random.randint(0, rows - shape_size + 1)
            col = np.random.randint(0, cols - shape_size + 1)
            matrix[row:row + shape_size, col:col + shape_size] = color

        elif shape_type == 'circle':
            center_row = np.random.randint(shape_size // 2, rows - shape_size // 2)
            center_col = np.random.randint(shape_size // 2, cols - shape_size // 2)
            radius = shape_size // 2
            for i in range(rows):
                for j in range(cols):
                    if math.sqrt((i - center_row) ** 2 + (j - center_col) ** 2) <= radius:
                        matrix[i, j] = color

        elif shape_type == 'sprite':
            sprite = np.array([[0, color, color, 0],
                               [color, 0, 0, color],
                               [color, 0, 0, color],
                               [0, color, color, 0]])
            row = np.random.randint(0, rows - sprite.shape[0] + 1)
            col = np.random.randint(0, cols - sprite.shape[1] + 1)
            matrix[row:row + 4, col:col + 4] = sprite

        elif shape_type == 'triangle':
            triangle = np.tril(np.full((shape_size, shape_size), color, dtype=int))
            row = np.random.randint(0, rows - shape_size + 1)
            col = np.random.randint(0, cols - shape_size + 1)
            matrix[row:row + triangle.shape[0], col:col + triangle.shape[1]] = triangle

    return matrix


def apply_transformation(matrix, transformation_type):
    if transformation_type == 'flip_horizontal':
        return np.flip(matrix, axis=1)
    elif transformation_type == 'flip_vertical':
        return np.flip(matrix, axis=0)
    elif transformation_type == 'rotate_90':
        return np.rot90(matrix, k=1)
    elif transformation_type == 'rotate_180':
        return np.rot90(matrix, k=2)
    elif transformation_type == 'rotate_270':
        return np.rot90(matrix, k=3)
    else:
        return matrix


def matrix_to_string(matrix):
    result = "[ "
    for row in matrix:
        result += ' '.join(map(str, row)) + ' '
    result += "]"
    return result


def visualize_matrix(matrix: str):
    for row in matrix:
        print('[', end=' ')
        for value in row:
            print(value, end=' ')
        print(']')