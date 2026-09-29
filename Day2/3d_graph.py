import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1. Create the 1D ranges
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

# 2. Generate the Meshgrid
X, Y = np.meshgrid(x, y)                        # meshgrid is a function used to create a rectangular grid out of two or more 1D arrays representing Cartesian coordinates

# 3. Calculate Z based on X and Y matrices
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R) / R

# 4. Plotting
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# cmap='viridis' adds a color gradient based on height (Z-axis)
surface = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

ax.set_title("3D Surface Plot using Meshgrid")
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_zlabel("Z axis")

plt.show()