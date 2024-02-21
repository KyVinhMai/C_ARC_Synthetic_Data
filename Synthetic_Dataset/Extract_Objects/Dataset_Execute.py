import random
import Extract_Object_Composer  as EOC

og = []
trans_mat = []
transformation = []
num_of_objects = []
dimensions = []

row = 15
column = 15
num_of_shapes = random.randint(1, 2)
transforms = [t for t in operations.keys()]
colors = [k for k in color_encoding.keys()]
shapes = ['square', 'circle', 'sprite', 'triangle']

for transform in transforms:
    num = 0
    for shape_type in shapes:
        shape_size = 4
        for r in range(9, row):
            for c in range(9, column):
                if r > 12 or c > 12:
                    num_of_shapes = random.randint(1, 3)
                    shape_size = random.randint(2, 5)
                original_matrix = generate_random_matrix(r, c, num_of_shapes, shape_size, shape_type)
                transformed_matrix = apply_transformation(original_matrix, transformation_type)

                unique_values = np.unique(original_matrix)
                num_of_shapes = len(unique_values[1:]) if len(unique_values) > 1 else 0
                matrix_list = original_matrix.tolist()
                og.append(matrix_list)
                trans_mat.append(transformed_matrix.tolist())
                transformation.append(transform)
                num_of_objects.append(num_of_shapes)
                dimensions.append([r, c])

                print("Original Matrix:", r, c)
                print(f"There are {num_of_shapes} object(s)")
                visualize_matrix(original_matrix)
                print("\nTransformed Matrix:", transform, r, c)
                print(f"There are {num_of_shapes} object(s)")
                visualize_matrix(transformed_matrix)
                num += 1
                print(num)


