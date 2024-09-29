import numpy as np
import matplotlib.pyplot as plt

# Sample data: Create a 10x10 matrix with random values
data = np.random.rand(10, 10)

# Create a heatmap using imshow
plt.imshow(data, cmap='inferno', interpolation='nearest')

# Add a colorbar to indicate the scale
plt.colorbar(label='Intensity')

# Set titles and labels
plt.title('Heatmap Example')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')

# Display the heatmap
plt.show()
