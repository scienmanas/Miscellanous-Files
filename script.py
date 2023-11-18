import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

print("[Script Started]")

# Assuming you have digitized data for equilibrium and operating lines
equilibrium_line_x = np.array([0, 0.04, 0.08, 0.12, 0.16, 0.24, 0.28, 0.32, 0.36, 0.4, 0.44, 0.48, 0.52, 0.56, 0.6, 0.64, 0.68, 0.72, 0.76, 0.8, 0.84, 0.88, 0.92, 0.96, 1.0])
equilibrium_line_y = np.array([0, 0.08, 0.16, 0.24, 0.335, 0.44, 0.48, 0.52, 0.57, 0.605, 0.651, 0.681, 0.72, 0.77, 0.79, 0.82, 0.845, 0.865, 0.89, 0.91, 0.93, 0.95, 0.96, 0.98, 1.0])

operating_line_x_set1 = np.array([0.03, 0.1, 0.2, 0.3, 0.4, 0.5, 0.58])
operating_line_y_set1 = 1.14 * operating_line_x_set1 + 0

operating_line_x_set2 = np.array([0.59, 0.6, 0.7, 0.8, 0.9, 1.0])
operating_line_y_set2 = 0.8 * operating_line_x_set2 + 0.196

linear_line_x = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.58, 0.6, 0.7, 0.8, 0.9, 1.0])
linear_line_y = linear_line_x

# Feed Line
x_feed = np.array([0.58, 0.59, 0.60, 0.61, 0.62])
y_feed = 7.0606 * (x_feed - 0.58) + 0.58

# Plot the lines
plt.plot(equilibrium_line_x, equilibrium_line_y, label='Equilibrium Line', linestyle='--', color='blue')
plt.plot(operating_line_x_set1, operating_line_y_set1, label='Operating Line Set 1', linestyle='--', color='green')
plt.plot(operating_line_x_set2, operating_line_y_set2, label='Operating Line Set 2', linestyle='--', color='purple')
plt.plot(linear_line_x, linear_line_y, label="Linear Line", linestyle='--', color='orange')
plt.plot(x_feed, y_feed, label="Feed Line", linestyle="-", color="brown")

# Interpolate equilibrium and operating lines for both sets
equilibrium_interpolated = interp1d(equilibrium_line_x, equilibrium_line_y, kind='linear', fill_value="extrapolate")
operating_interpolated_set1 = interp1d(operating_line_x_set1, operating_line_y_set1, kind='linear', fill_value="extrapolate")
operating_interpolated_set2 = interp1d(operating_line_x_set2, operating_line_y_set2, kind='linear', fill_value="extrapolate")

# Find intersection points (stages) for both sets
intersection_points_y_set1 = equilibrium_interpolated(operating_line_x_set1)
intersection_points_y_set2 = equilibrium_interpolated(operating_line_x_set2)

# Plot the intersection points
plt.scatter(operating_line_x_set1, intersection_points_y_set1, color='red', label='Intersection Points Set 1')
plt.scatter(operating_line_x_set2, intersection_points_y_set2, color='blue', label='Intersection Points Set 2')

# Plot the stages and horizontal lines for both sets
for x_set1, y_eq_set1, y_op_set1 in zip(operating_line_x_set1, intersection_points_y_set1, operating_line_y_set1):
    plt.plot([x_set1, x_set1], [y_eq_set1, y_op_set1], color='black', linestyle='--', linewidth=0.8)
    plt.plot([0, x_set1], [y_op_set1, y_op_set1], color='gray', linestyle='--', linewidth=0.8)

for x_set2, y_eq_set2, y_op_set2 in zip(operating_line_x_set2, intersection_points_y_set2, operating_line_y_set2):
    plt.plot([x_set2, x_set2], [y_eq_set2, y_op_set2], color='black', linestyle='--', linewidth=0.8)
    plt.plot([0, x_set2], [y_op_set2, y_op_set2], color='gray', linestyle='--', linewidth=0.8)

# Count the number of stages for both sets
num_stages_set1 = np.sum(intersection_points_y_set1 > operating_line_y_set1)
num_stages_set2 = np.sum(intersection_points_y_set2 > operating_line_y_set2)

# Print the results
print(f"Number of equilibrium stages Set 1: {num_stages_set1}")
print(f"Number of equilibrium stages Set 2: {num_stages_set2}")

plt.xlabel('x-axis (xa)')
plt.ylabel('y-axis (ya)')

# Show the plot
plt.legend()
plt.show()
