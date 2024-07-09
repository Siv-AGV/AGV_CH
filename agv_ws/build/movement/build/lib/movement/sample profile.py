import numpy as np
import matplotlib.pyplot as plt

# Given values
v_max = 1.5  # m/s
d = 1      # meters

# Calculate acceleration and deceleration distances
d_acceleration = d_deceleration = d / 4

# Time for acceleration and deceleration phases
t_acceleration = v_max / (v_max / d_acceleration)
t_deceleration = v_max / (v_max / d_deceleration)

# Time for constant speed phase
d_constant_speed = d - 2 * d_acceleration
t_constant_speed = d_constant_speed / v_max

# Time array
t_total = t_acceleration + t_constant_speed + t_deceleration
t = np.linspace(0, t_total, 1000)

# Speed profile using sinusoidal functions for smooth transitions
speed = np.piecewise(t, [t < t_acceleration,
                         (t >= t_acceleration) & (t <= t_acceleration + t_constant_speed),
                         t > t_acceleration + t_constant_speed],
                     [lambda t: v_max * (1 - np.cos(np.pi * t / t_acceleration)) / 2,
                      v_max,
                      lambda t: v_max * (1 + np.cos(np.pi * (t - t_acceleration - t_constant_speed) / t_deceleration)) / 2])

# Plot
plt.plot(t, speed)
plt.xlabel('Time (s)')
plt.ylabel('Speed (m/s)')
plt.title('Smooth AGV Speed Profile')
plt.grid(True)
plt.show()
