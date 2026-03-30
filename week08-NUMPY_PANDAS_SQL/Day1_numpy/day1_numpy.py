import numpy as np

"""
Concept: Python list vs NumPy array
"""

my_list = [1, 2, 3, 4] * 2
print(my_list)
print(type(my_list))  # list repeats values

array = np.array([1, 2, 3, 4]) * 2
print(array)
print(type(array))  # numpy does element-wise multiplication


"""
Concept: shape, ndim, and indexing in 3D array
"""

array = np.array(
    [
        [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]],
        [["J", "K", "L"], ["M", "N", "O"], ["P", "Q", "R"]],
        [["S", "T", "Q"], ["V", "U", "W"], ["X", "Y", "Z"]],
    ]
)

picked_letters = array[0, 1, 2] + array[0, 2, 2] + array[2, 1, 2]

print(array.shape)  # layers, rows, columns
print(array.ndim)  # number of dimensions
print(picked_letters)  # indexing in 3D array


"""
Concept: slicing in 2D array
"""

array = np.array(
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]
)

print(array.shape)
print(array[0:4:2])  # row slicing with step
print(array[::-2])  # reverse rows with step
print(array[:, 0:4])  # all rows, all columns
print(array[:, 2:])  # all rows, columns from index 2
print(array[0:2, 0:2])  # top-left block
print(array[2:4, 1:3])  # middle block


"""
Concept: dtype and memory
"""

array = np.array([1, 2, 3, 4], dtype=np.int16)

print(array)
print(array.dtype)
print(f"this using {array.nbytes} bytes")
