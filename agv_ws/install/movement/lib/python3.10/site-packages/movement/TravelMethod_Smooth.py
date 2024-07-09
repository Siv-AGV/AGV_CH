import numpy as np
import matplotlib.pyplot as plt

def s_curve_velocity_profile(distance, v_max, a_max, j_max):
    # Time to reach max acceleration
    t_j = a_max / j_max
    # Time to reach max velocity
    t_a = v_max / a_max
    # Distance to reach max acceleration
    d_j = (1/6) * j_max * t_j**3
    # Distance to reach max velocity
    d_a = 0.5 * a_max * t_a**2

    if distance < 2 * d_a:
        # If the distance is too short to reach v_max, we calculate the adjusted profile
        t_a = np.sqrt(distance / (2 * a_max))
        v_peak = a_max * t_a
        t_total = 2 * t_a

        times = np.linspace(0, t_total, num=1000)
        velocities = np.zeros_like(times)

        for i, t in enumerate(times):
            if t < t_a:
                velocities[i] = a_max * t
            else:
                velocities[i] = v_peak - a_max * (t - t_a)
    else:
        # Calculate the distance traveled at constant velocity
        d_const = distance - 2 * d_a
        t_const = d_const / v_max

        t_total = 2 * t_a + t_const

        times = np.linspace(0, t_total, num=1000)
        velocities = np.zeros_like(times)

        for i, t in enumerate(times):
            if t < t_j:
                velocities[i] = 0.5 * j_max * t**2
            elif t < t_j + t_a:
                velocities[i] = a_max * (t - t_j) + 0.5 * j_max * t_j**2
            elif t < t_j + t_a + t_const:
                velocities[i] = v_max
            elif t < t_j + t_a + t_const + t_j:
                t_decel = t - (t_j + t_a + t_const)
                velocities[i] = v_max - 0.5 * j_max * t_decel**2
            elif t < t_total - t_j:
                t_decel = t - (t_j + t_a + t_const + t_j)
                velocities[i] = v_max - a_max * t_decel - 0.5 * j_max * t_j**2
            else:
                t_decel = t - (t_total - t_j)
                velocities[i] = 0.5 * j_max * (t_total - t - t_j)**2

    return times, velocities

# Parameters
distance = 10  # Example distance in meters
v_max = 1.5  # Max linear speed in meters/second
a_max = 0.5  # Max acceleration in meters/second^2
j_max = 1.0  # Max jerk in meters/second^3

# Generate the velocity profile
times, velocities = s_curve_velocity_profile(distance, v_max, a_max, j_max)

# Plot the velocity profile
plt.plot(times, velocities)
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.title('S-Curve Velocity Profile')
plt.grid(True)
plt.show()
