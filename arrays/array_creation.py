import numpy as np

# Creating arrays
array_1d = np.array([1, 2, 3, 4])
array_2d = np.array([[1, 2], [3, 4]])

# Creating arrays filled with zeros, ones, or random numbers
zeros_array = np.zeros((3, 3))  # 3x3 matrix of zeros
ones_array = np.ones((2, 4))    # 2x4 matrix of ones
random_array = np.random.rand(3, 2)  # 3x2 matrix of random floats

# Array filled with a constant value
constant_array = np.full((2, 3), 7)

# Basic operations
array_sum = array_1d + 10
elementwise_product = array_1d * 2

# Printing arrays
print("1D Array:", array_1d)
print("2D Array:", array_2d)
print("Zeros Array:", zeros_array)
print("Ones Array:", ones_array)
print("Random Array:", random_array)
print("Constant Array:", constant_array)
print("Sum Array:", array_sum)
print("Elementwise Product:", elementwise_product)
