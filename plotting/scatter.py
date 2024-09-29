import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create scatter plot
plt.scatter(x, y, color='blue', marker='o')

# Adding titles and labels
plt.title('Basic Scatter Plot')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')

# Display the plot
plt.grid(True)  # Add grid for better visibility
plt.show()
