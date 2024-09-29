import numpy as np

# Creating a 2D array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Aggregations
array_sum = np.sum(array)
array_mean = np.mean(array)
array_max = np.max(array)

# Aggregation along axis
row_sum = np.sum(array, axis=1)
column_sum = np.sum(array, axis=0)

print("Array Sum:", array_sum)
print("Array Mean:", array_mean)
print("Array Max:", array_max)
print("Row-wise Sum:", row_sum)
print("Column-wise Sum:", column_sum)
