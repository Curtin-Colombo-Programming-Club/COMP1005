import numpy as np

# Creating a 2D array
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Indexing a single element
element = array[1, 2]  # Element at row 1, column 2 (zero-based)

# Slicing rows and columns
row_slice = array[1, :]  # Second row
column_slice = array[:, 1]  # Second column

# Slicing sub-matrices
sub_matrix = array[0:2, 1:3]  # First two rows, columns 1 and 2

# Fancy indexing
selected_elements = array[[0, 2], [1, 0]]  # Select (0,1) and (2,0)

print("Original Array:\n", array)
print("Selected Element:", element)
print("Row Slice:", row_slice)
print("Column Slice:", column_slice)
print("Sub-matrix:\n", sub_matrix)
print("Fancy Indexing Result:", selected_elements)
