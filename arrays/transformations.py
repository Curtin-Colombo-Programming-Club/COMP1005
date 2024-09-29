import numpy as np

# Creating a 2D array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Reshaping the array
reshaped_array = array.reshape((3, 2))  # Reshape to 3x2 matrix

# Transposing the array
transposed_array = array.T  # Transpose rows and columns

# Flattening the array to 1D
flattened_array = array.flatten()

print("Original Array:\n", array)
print("Reshaped Array:\n", reshaped_array)
print("Transposed Array:\n", transposed_array)
print("Flattened Array:", flattened_array)
