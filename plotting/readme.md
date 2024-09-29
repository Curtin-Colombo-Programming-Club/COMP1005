# Plotting Examples with Matplotlib

This folder contains a collection of plotting examples using **Matplotlib**. Each example demonstrates how to create various types of plots, from basic scatter plots to more advanced visualizations like subplots and RGB images.

## Files Overview

1. **`scatter_plot.py`**
2. **`subplots.py`**
3. **`imshow_heatmap.py`**
4. **`imshow_rgb.py`**
5. **`random_rgb_array.py`**

---

## 1. Scatter Plot Example (`scatter_plot.py`)

This script demonstrates how to create a **scatter plot** in Matplotlib. Scatter plots are useful for visualizing the relationship between two variables.

### Key Features:
- Plots points based on random `x` and `y` values.
- Adds a title and axis labels.
- Uses the `scatter()` function.

### Usage:
```python
python scatter_plot.py
```

### Output:
A scatter plot with random data points displayed on a 2D grid.

---

## 2. Subplots Example (`subplots.py`)

This script demonstrates how to create multiple **subplots** in a single figure. Subplots allow you to display multiple plots side by side or one above the other.

### Key Features:
- Two subplots arranged side by side.
- Two subplots arranged one above the other.
- Uses the `subplot()` function to organize multiple plot areas.

### Usage:
```python
python subplots.py
```

### Output:
A figure with two subplots arranged in different configurations (side by side and one on top of the other).

---

## 3. Heatmap Example with `imshow` (`imshow_heatmap.py`)

This script demonstrates how to create a **heatmap** using Matplotlib’s `imshow()` function. Heatmaps are useful for visualizing 2D data with color coding.

### Key Features:
- Generates a 2D random array with values ranging between 0 and 1.
- Visualizes the array as a heatmap.
- Uses a colorbar to indicate the range of values.

### Usage:
```python
python imshow_heatmap.py
```

### Output:
A heatmap showing random values in a 2D grid, with a color gradient representing the data values.

---

## 4. Custom RGB Array with `imshow` (`imshow_rgb.py`)

This script shows how to use `imshow()` to visualize a **custom RGB image** generated from a 3D array. The RGB array defines the color of each pixel in the image.

### Key Features:
- Creates a 100x100 RGB array where each pixel is assigned a unique color.
- The color is a gradient based on the row and column positions.
- Displays the array as an image.

### Usage:
```python
python imshow_rgb.py
```

### Output:
An image with a color gradient representing the RGB values of each pixel in the array.

---

## 5. Random RGB Array Example (`random_rgb_array.py`)

This script demonstrates how to create an image with **random RGB values** using `imshow()`. Each pixel is assigned a random color by generating a 3D array.

### Key Features:
- Generates a 50x50 pixel image.
- Each pixel has random RGB values (between 0 and 1).
- Displays the random image using `imshow()`.

### Usage:
```python
python random_rgb_array.py
```

### Output:
A 50x50 pixel image with randomly assigned colors.

---

## How to Run the Scripts

To run any of the scripts, simply execute the Python file using the following command:

```bash
python <filename.py>
```

Make sure you have **Matplotlib** installed. If not, install it via:

```bash
pip install matplotlib
```

---

## Summary

These examples provide a variety of plotting techniques using Matplotlib. Whether you're plotting scatter points, creating subplots, or displaying RGB images, these scripts serve as a foundation for visual data representation.

