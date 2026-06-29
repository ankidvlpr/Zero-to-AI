import numpy as np
from numpy.linalg import *

#Linear algebra using numpy
# matrix calculation -> solve, dot product, inner, outer, determinant, inverse, trace


# DOT product
array1 = np.array([1,2,3,4,5])
array2 = np.array([6,7,8,9,3])

print("Dot product:",np.dot(array1, array2))

# 2d dim dot product

brr1 = np.array([[1,2,3],
                 [4,5,6],
                 [1,2,3]])

brr2 = np.array([[6,7,8],
                 [1,2,3],
                 [1,2,3]])

print(brr1.shape)
print(brr2.shape)
print("Dot product of 2D:", np.dot(brr1,brr2))


# finding x ,y , z ,  solve 2x +  y  + z =  5
#                          x  +  2y + z =  6
#                          x  +  y  + 2z = 7

#  by Ax = B 

array1 = np.array([[2,1,1],
                   [1,2,1],
                   [1,1,2]])
array2 = np.array([5,6,7])

x,y,z = solve(array1, array2)

print(f"x = {x},y = {y},z = {z}")


# matrix multiplication example

a = np.array([[1,2],
              [2,3],
              [3,4]])
b = np.array([[1,2,3,4],
              [2,3,3,4]])

print(a@b)  # (3,2) @ (2,4) -> output shape becomes (3,4)


# numpy.linalg.norm(x, ord=None, axis=None)
# by default the norms is set to forbinus norm which is square root of array
vector = np.array([3,4])

norm = np.linalg.norm(vector)

print(norm)

# here is a norm of matrix

array = np.array([[1,2,3],
                  [2,3,4]])

norm = np.linalg.norm(array)
print(norm)


# common norm types

# ord=1   #L1 norm manhattan distance
# ord=2   #L2 norm Ecluidean distance
# ord=np.inf # infinty norm (max absolute distance)
# ord='fro'  # forbenius norm (matrix default)



vector = np.array([3,4])

lnorm = np.linalg.norm(vector)
l1_norm = np.linalg.norm(vector, ord=1)
l2_norm = np.linalg.norm(vector, ord=2)
l3_norm = np.linalg.norm(vector, ord=np.inf)

print(lnorm)
print(l1_norm)
print(l2_norm)
print(l3_norm)
