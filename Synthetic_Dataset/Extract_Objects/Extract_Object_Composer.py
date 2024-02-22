import numpy as np
import math
import random
import utils.helper_functions as hf

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

#Constraints
#num of objects
#Probablity of it being the same color or different color
#Size of matrix min(10,10)
#action no action

class matrix_generator:
    def __init__(self, rows, cols, shape_size):
        self.shape_size = shape_size
        self.color_inventory = [1, 2, 3, 4, 5, 6, 7, 8, 9]# Does not include 0
        self.rows = rows
        self.cols = cols
        self.background_color = None
        self.target_color = None
        self.tags = {
            "background": "",
            "num_of_objects": "", #todo have background objects add to the count
            "colors": []
        }

    def pick_color(self, replace=True):
        if replace:
            return np.random.choice(self.color_inventory)

        color = np.random.choice(self.color_inventory)
        self.color_inventory.remove(color)
        return color

    def background(self) -> np.array:
        choice = random.choices(["empty", "solid", "lines", "noise"], weights=[3, 2, 2, 2])[0] #todo Implement Objects

        if choice == "empty":
            self.tags['background'] = "empty"
            return np.zeros((self.rows, self.cols), dtype=int)

        elif choice == "solid":
            "Select whether the solid background will be in the center or offset"
            self.background_color = self.pick_color(False)
            self.tags['background'] = "solid"
            return hf.gen_square_background(self.rows, self.cols, self.background_color)

        elif choice == "lines":
            backdrop = random.choice(["vertical", "horizontal"]) #todo implement diagonal lines
            self.background_color = self.pick_color(True)

            if backdrop == "horizontal":
                self.tags["background"] = "horizontal_lines"
                return hf.gen_horizontal_lines(self.rows, self.cols, self.background_color)

            elif backdrop == "vertical":
                self.tags["background"] = "vertical_lines"
                return hf.gen_vertical_lines(self.rows, self.cols, self.background_color)

        elif choice == "noise":
            self.tags["background"] = "noise"
            self.background_color = self.pick_color(True)
            return hf.gen_noisy_matrix(self.rows, self.cols, self.background_color)


    def target_object(self):
        assert self.background_color not in self.tags["solid_background"], \
            "Object is the same color as solid background"
        shape = random.choices(["square", "circle", "sprite"], weights=[2, 1, 1])[0]

        if shape == 'square':
            row = np.random.randint(0, rows - shape_size + 1)
            col = np.random.randint(0, cols - shape_size + 1)
        elif shape ==


    def apply_target_to_background(self):
        pass


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

if __name__ == "__main__":
    gen = matrix_generator(10, 10, 5)
    matrix = gen.background()
    print(gen.tags)
    print(gen.background_color)
    print(gen.color_inventory)
    print()
    visualize_matrix(matrix)