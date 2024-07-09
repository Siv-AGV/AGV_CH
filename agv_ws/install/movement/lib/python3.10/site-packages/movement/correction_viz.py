import numpy as np
import matplotlib.pyplot as plt

# Parameters
wheel_radius = 0.0875
wheel_separation = 0.657
max_speed = 1.5
max_acceleration = 0.2

# Speed conversion matrix
speed_conversion = np.array([[wheel_radius / 2, wheel_radius / 2],
                             [wheel_radius / wheel_separation, -wheel_radius / wheel_separation]])

# Function to calculate trapezoidal velocity profile
def trapezoidal_velocity_profile(distance, max_speed, max_acceleration, traveled_distance):
    if distance == 0:
        return 0.0

    t_acc = max_speed / max_acceleration
    d_acc = 0.5 * max_acceleration * t_acc**2

    if distance < 2 * d_acc:
        v_peak = np.sqrt(max_acceleration * distance)
        t_acc = v_peak / max_acceleration
        d_acc = 0.5 * max_acceleration * t_acc**2

    if traveled_distance < d_acc:
        velocity = np.sqrt(2 * max_acceleration * traveled_distance)
    elif traveled_distance < distance - d_acc:
        velocity = max_speed
    else:
        velocity = np.sqrt(2 * max_acceleration * (distance - traveled_distance))

    return velocity

# Function to calculate corrections
def calculate_corrections(offset_x, offset_y, offset_z):
    linear_correction = np.sqrt(offset_x**2 + offset_y**2)
    angular_correction = offset_z
    agv_correction = np.array([[linear_correction], [angular_correction]])
    wheel_speed_correction = np.matmul(np.linalg.inv(speed_conversion), agv_correction)
    return wheel_speed_correction.flatten()

# Simulate AGV movement with corrections
def simulate_agv_movement(initial_distance, offsets, time_step=0.1):
    traveled_distance = 0.0
    path = []
    original_wheel_speeds = []
    corrected_wheel_speeds = []

    while traveled_distance < initial_distance:
        # Calculate original wheel speeds
        linear_speed = trapezoidal_velocity_profile(initial_distance, max_speed, max_acceleration, traveled_distance)
        agv_speed = np.array([[linear_speed], [0.0]])
        original_wheel_speed = np.matmul(np.linalg.inv(speed_conversion), agv_speed).flatten()
        original_wheel_speeds.append(original_wheel_speed)

        # Apply corrections if more than 1.5m left to travel
        if initial_distance - traveled_distance > 1.5:
            correction = calculate_corrections(offsets[0], offsets[1], offsets[2])
            corrected_wheel_speed = original_wheel_speed + correction
        else:
            corrected_wheel_speed = original_wheel_speed

        corrected_wheel_speeds.append(corrected_wheel_speed)

        # Update traveled distance
        traveled_distance += linear_speed * time_step
        path.append(traveled_distance)

    return path, original_wheel_speeds, corrected_wheel_speeds

# Visualization function
def visualize_agv_movement(path, original_wheel_speeds, corrected_wheel_speeds):
    plt.figure(figsize=(10, 6))
    plt.plot(path, [ws[0] for ws in original_wheel_speeds], label='Original Left Wheel Speed', linestyle='--')
    plt.plot(path, [ws[1] for ws in original_wheel_speeds], label='Original Right Wheel Speed', linestyle='--')
    plt.plot(path, [ws[0] for ws in corrected_wheel_speeds], label='Corrected Left Wheel Speed')
    plt.plot(path, [ws[1] for ws in corrected_wheel_speeds], label='Corrected Right Wheel Speed')
    plt.xlabel('Distance Traveled (m)')
    plt.ylabel('Wheel Speed (m/s)')
    plt.title('AGV Wheel Speeds with Corrections')
    plt.legend()
    plt.grid(True)
    plt.show()

# Input distance and offsets at the first station
initial_distance = 5.0  # Example distance in meters
offsets = [0.05, 0.05, 0.02]  # Example offsets in meters and radians

# Simulate and visualize AGV movement
path, original_wheel_speeds, corrected_wheel_speeds = simulate_agv_movement(initial_distance, offsets)
visualize_agv_movement(path, original_wheel_speeds, corrected_wheel_speeds)
