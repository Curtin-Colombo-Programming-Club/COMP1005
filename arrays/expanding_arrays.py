import numpy as np

# Creating a 1D array
array = np.array([1, 2, 3])

# Expanding dimensions
expanded_array = np.expand_dims(array, axis=0)  # Convert to 2D (1x3)
expanded_array_2 = np.expand_dims(array, axis=1)  # Convert to 2D (3x1)

# Stacking arrays
array2 = np.array([4, 5, 6])
stacked_array = np.vstack([array, array2])  # Stack vertically
concatenated_array = np.concatenate((array, array2), axis=0)  # Concatenate along axis 0

print("Original Array:", array)
print("Expanded Array (Axis=0):", expanded_array)
print("Expanded Array (Axis=1):\n", expanded_array_2)
print("Vertically Stacked Arrays:\n", stacked_array)
print("Concatenated Array:", concatenated_array)
