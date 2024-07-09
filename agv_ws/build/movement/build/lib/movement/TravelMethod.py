import numpy as np
import matplotlib.pyplot as plt

def trapezoidal_velocity_profile(distance, v_max, a_max):
    # Time to reach max velocity
    t_acc = v_max / a_max
    # Distance to reach max velocity
    d_acc = 0.5 * a_max * t_acc**2

    if distance < 2 * d_acc:
        # If the distance is too short to reach v_max, we calculate the adjusted profile
        t_acc = np.sqrt(distance / (2 * a_max))
        v_peak = a_max * t_acc
        t_total = 2 * t_acc

        times = np.linspace(0, t_total, num=1000)
        velocities = np.zeros_like(times)

        for i, t in enumerate(times):
            if t < t_acc:
                velocities[i] = a_max * t
            else:
                velocities[i] = v_peak - a_max * (t - t_acc)
    else:
        # Calculate the distance traveled at constant velocity
        d_const = distance - 2 * d_acc
        t_const = d_const / v_max

        t_total = 2 * t_acc + t_const

        times = np.linspace(0, t_total, num=1000)
        velocities = np.zeros_like(times)

        for i, t in enumerate(times):
            if t < t_acc:
                velocities[i] = a_max * t
            elif t < t_acc + t_const:
                velocities[i] = v_max
            else:
                t_decel = t - t_acc - t_const
                velocities[i] = v_max - a_max * t_decel

    return times, velocities

# Parameters
distance = 10  # Example distance in meters
v_max = 1.5  # Max linear speed in meters/second
a_max = 0.5  # Max acceleration in meters/second^2

# Generate the velocity profile
times, velocities = trapezoidal_velocity_profile(distance, v_max, a_max)

# Plot the velocity profile
plt.plot(times, velocities)
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.title('Trapezoidal Velocity Profile')
plt.grid(True)
plt.show()
