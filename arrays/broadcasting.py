import numpy as np

# Creating arrays
array1 = np.array([1, 2, 3])
array2 = np.array([[10], [20], [30]])

# Broadcasting addition
result = array1 + array2  # Adds array1 to each row of array2

print("Array 1:", array1)
print("Array 2:\n", array2)
print("Result of Broadcasting:\n", result)
