# NumPy Array Functionalities

This folder contains a collection of Python scripts demonstrating key functionalities of NumPy arrays. These examples cover core operations useful for both plotting and working with class collections. The goal is to provide a reference for efficiently manipulating and processing data using NumPy, without directly involving plotting.

## List of Files

1. **`array_creation.py`**  
   Demonstrates how to create NumPy arrays using different methods (e.g., arrays of zeros, ones, random values, and constants) and perform basic operations like addition and multiplication.

2. **`slicing_indexing.py`**  
   Covers array slicing and indexing techniques. You'll learn how to select individual elements, slices of rows or columns, and sub-arrays from a larger array.

3. **`expanding_arrays.py`**  
   Shows how to expand dimensions of arrays using `np.expand_dims()` and demonstrates array concatenation and stacking operations.

4. **`transformations.py`**  
   Demonstrates reshaping, transposing, and flattening of arrays, which are essential for restructuring data in different formats.

5. **`broadcasting.py`**  
   Explains the concept of broadcasting, which allows arrays of different shapes to be combined in mathematical operations.

6. **`boolean_masking.py`**  
   Demonstrates the use of Boolean masking to filter arrays based on certain conditions, providing an easy way to extract specific elements.

7. **`aggregations.py`**  
   Shows how to use aggregation functions like `sum()`, `mean()`, and `max()` to reduce arrays to scalar values or apply these operations along specific axes (e.g., row-wise or column-wise).

---

## Key Concepts

### 1. **Array Creation**
   - Learn how to create arrays with specific dimensions and contents, such as zeros, ones, or random values.
   - Example operations: elementwise addition, multiplication.

### 2. **Slicing and Indexing**
   - Master array slicing to extract rows, columns, sub-arrays, and specific elements from an array.
   - Understand the concept of fancy indexing for more complex element selection.

### 3. **Expanding and Concatenating Arrays**
   - Expand arrays along new axes using `np.expand_dims()`.
   - Stack arrays vertically or horizontally and concatenate arrays.

### 4. **Transformations**
   - Reshape arrays into different dimensionalities, transpose rows and columns, and flatten arrays to 1D.
   - Essential for transforming data into formats required for analysis.

### 5. **Broadcasting**
   - Use broadcasting to combine arrays of different shapes in mathematical operations without manual reshaping.

### 6. **Boolean Masking**
   - Apply conditions to arrays and filter elements based on these conditions using Boolean arrays as masks.

### 7. **Aggregations**
   - Perform operations like summing or averaging over entire arrays or specific axes.
   - Useful for reducing data in statistics and analysis.

---

## Usage

Each file can be run individually to explore specific NumPy operations. To run a script, use:

```bash
python <filename>.py
```

For example:

```bash
python array_creation.py
```

Each script will print the results of the demonstrated operations, making it easy to understand how NumPy works under the hood.

---

## Summary

This collection of examples serves as a foundation for understanding and applying essential NumPy operations. Whether you're working with data processing, class collections, or preparing data for visualization, these scripts provide useful insights into the versatility of NumPy arrays.

--- 

Programming Club of Curtin Colombo
