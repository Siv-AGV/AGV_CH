import matplotlib.pyplot as plt
import numpy as np

# Update the diagram to correct the x-axis alignment with the AGV direction

# Define the new AGV positions and orientations based on the updated x-axis alignment
positions = {
    'Forward': 180,
    'Right': -90,
    'Left': 90,
    'Rear': 0
}

# Define the new plot
fig, ax = plt.subplots()
ax.axhline(0, color='grey', lw=0.5)
ax.axvline(0, color='grey', lw=0.5)
ax.grid(True, which='both')

# Set the limits of the plot
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# Plot the new AGV orientations
for direction, angle in positions.items():
    x = np.cos(np.radians(angle))
    y = np.sin(np.radians(angle))
    ax.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, label=f'{direction} ({angle}°)')

# Define the new annotations for the directions
annotations = {
    'Center': (0, 0),
    'Forward (+x)': (1, 0),
    'Rear (-x)': (-1, 0),
    'Right (-y)': (0, -1),
    'Left (+y)': (0, 1)
}

# Plot the new annotations
for label, (x, y) in annotations.items():
    ax.text(x, y, label, fontsize=12, ha='center')

# Set the labels and title
ax.set_xlabel('X-axis (m)')
ax.set_ylabel('Y-axis (m)')
ax.set_title('Corrected AGV Orientations and XY Directions')
ax.legend()

# Display the plot
plt.show()
