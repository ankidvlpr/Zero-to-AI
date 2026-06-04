import numpy as np

# Scalar arithmetic

array = np.array([1,2,3,4,5])

print(array + 1)
print(array - 3)
print(array * 4 )
print(array / 2)
print(array ** 2)


# Vectorized math func

print(np.sqrt(array))
print(np.round(array))
print(np.pi)

# area of circle
radii = np.array([1, 2, 3])
print(np.pi * radii ** 2)

#Element wise arthmetic

array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)
print(array1 ** array2)

# Comparsion operator

marks = np.array([23,56,78,90, 99])

print(marks == 90)
marks[marks < 75] = 0
print(marks)


""" BROADCASTING """

array1 = np.array([[1,2,3,4]])
array2 = np.array([[1],[2],[3],[4]])

print(array1.shape)
print(array2.shape)

# rule - dimensional should be match or be 1 
print(array1 * array2)



# Aggregate Functions = summaize data and typically
#                        return a single value

array = np.array([[1,2,3,4,6,7],
                  [5,6,7,8,8,6]])

print(np.sum(array))
print(np.mean(array))
print(np.min(array))
print(np.max(array))
print(np.std(array)) 
print(np.var(array))
print(np.argmin(array))  # index of min
print(np.argmax(array))  # index of max

print(np.where(array))
print(np.unique(array))


print(np.sum(array, axis=0))  # column wise
print(np.sum(array, axis=1))  # row wise


"""
Filtering = refering the process of selcting elements from an array 
that matches the given condtion

"""


ages = np.array([[21,19,12,40,20,65],
                 [39,22,15,99,19,50]])


teenager = ages[ages<18]
adult = ages[(ages >= 18) & (ages <=65)]

print(teenager)
print(adult)
print(teenager.ndim)

"""np.where()"""

print(np.where(ages <= 18, ages, -1))   # condition | value | fill value



"""random number by numpy"""


rng = np.random.default_rng(42)

print(rng.integers(low=1,high=7, size=(2,3)))

# for floating and equal chances we use uniform()

array = np.random.uniform(low=1,high=5, size=(2,3))
print(array)


"""Shuffle the array """

array = np.array([1,2,3,4,5])

rng = np.random.default_rng(42)

rng.shuffle(array)
print(array)


# for fruits

fruits = np.array(['apple','orange','banana','graphes'])

rng = np.random.default_rng(42)

fruit = rng.choice(fruits, size=(2,4))

print(fruit)
