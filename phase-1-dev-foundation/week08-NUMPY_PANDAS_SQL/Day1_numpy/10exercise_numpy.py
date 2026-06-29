import numpy as np

"""
Exercise 1: 1D Array Basics
Create a 1D NumPy array: [10, 20, 30, 40, 50]
Print the first and last element.
Find the length of the array.
"""

array = np.array([10, 20, 30, 40, 50])
print(array[0])
print(array[-1])
print(len(array))


"""
Exercise 2: 2D Array Creation
Create a 3x3 matrix.
Print the shape of the matrix.
Access the middle element.
"""

array1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(array1.shape)
print(array1[1, 1])


"""
Exercise 3: Slicing (1D)
Array: [1, 2, 3, 4, 5, 6, 7, 8]
Get the first 3 elements.
Get the last 3 elements.
Get the even index elements.
"""

array2 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(array2[0:3])  # first 3 elements
print(array2[-3:])  # last 3 elements
print(array2[::2])  # even index elements


"""
Exercise 4: Slicing (2D)
Use the same 3x3 matrix.
Extract the first row.
Extract the last column.
Extract the top-left 2x2 submatrix.
"""

array3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(array3[0])  # first row
print(array3[:, -1])  # last column
print(array3[0:2, 0:2])  # top-left 2x2


"""
Exercise 5: Reverse Array
Reverse the array [1, 2, 3, 4, 5] using slicing.
Do this without using a loop.
"""

array4 = np.array([1, 2, 3, 4, 5])
print(array4[::-1])


"""
Exercise 6: Sum and Mean
Array: [5, 10, 15, 20]
Calculate the total sum.
Calculate the mean (average).
"""

array5 = np.array([5, 10, 15, 20])
total_sum = np.sum(array5)
mean = np.mean(array5)

print(total_sum)
print(mean)


"""
Exercise 7: Axis Understanding
Take a 2D array:
[[1, 2, 3], [4, 5, 6]]
Calculate the row-wise sum (axis=1).
Calculate the column-wise sum (axis=0).
"""

array6 = np.array([[1, 2, 3], [4, 5, 6]])
row_sum = array6.sum(axis=1)
column_sum = array6.sum(axis=0)

print(row_sum)
print(column_sum)


"""
Exercise 8: Broadcasting
Array: [1, 2, 3, 4]
Add +10 to every element.
Multiply the array by 2.
"""

array7 = np.array([1, 2, 3, 4])
add = array7 + 10
multiply = array7 * 2

print(add)
print(multiply)


"""
Exercise 9: Condition Filtering
Array: [10, 15, 20, 25, 30]
Extract only those elements that are > 20.
"""

array8 = np.array([10, 15, 20, 25, 30])
array8 = array8[array8 > 20]
print(array8)


"""
Exercise 10: Combine Everything
Generate a random 4x4 array.
Find its:
Max value
Min value
Mean
Get the transpose of the array.
Reverse a single row.
"""

rng = np.random.default_rng(42)
random_array = rng.integers(low=1, high=20, size=(4, 4))
print(random_array)
print(np.max(random_array))
print(np.min(random_array))
print(np.mean(random_array))
print(random_array.T)

reversed_row_array = random_array.copy()
reversed_row_array[0] = reversed_row_array[0, ::-1]
print(reversed_row_array)  # only first row reversed
