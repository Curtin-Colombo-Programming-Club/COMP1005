import numpy as np
import matplotlib.pyplot as plt

# Define the dimensions of the image
height, width = 50, 50

# Create a random RGB array with values in the range [0, 1]
# The shape is (height, width, 3) for RGB channels
rgb_array = np.random.rand(height, width, 3)

# Create a heatmap using imshow
plt.imshow(rgb_array)

# Set titles and labels
plt.title('Random RGB Array Example (50x50)')
plt.xlabel('Width')
plt.ylabel('Height')

# Display the image
plt.axis('off')  # Turn off axis numbers and ticks
plt.show()
