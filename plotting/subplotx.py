import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2 = [1, 4, 6, 8, 10]

# Create a figure and a set of subplots (2 plots side by side)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# First subplot
ax1.scatter(x, y1, color='blue', marker='o')
ax1.set_title('Scatter Plot 1')
ax1.set_xlabel('X-axis Label')
ax1.set_ylabel('Y-axis Label')
ax1.grid(True)

# Second subplot
ax2.scatter(x, y2, color='red', marker='s')
ax2.set_title('Scatter Plot 2')
ax2.set_xlabel('X-axis Label')
ax2.set_ylabel('Y-axis Label')
ax2.grid(True)

# Adjust layout
plt.tight_layout()
plt.show()
