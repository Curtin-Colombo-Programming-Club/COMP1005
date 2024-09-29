import numpy as np

# Creating an array
array = np.array([1, 2, 3, 4, 5, 6])

# Boolean condition
mask = array > 3

# Applying the mask
filtered_array = array[mask]

print("Original Array:", array)
print("Mask:", mask)
print("Filtered Array:", filtered_array)
