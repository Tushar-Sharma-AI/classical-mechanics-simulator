import numpy as np
import matplotlib.pyplot as plt

g = 9.81

v0 = 50
theta_deg = 45

theta = np.radians(theta_deg)

t_flight = (2 * v0 * np.sin(theta)) / g

t = np.linspace(0, t_flight, 500)

x = v0 * np.cos(theta) * t
y = v0 * np.sin(theta) * t - 0.5 * g * t**2

plt.figure(figsize=(8, 5))
plt.plot(x, y)

plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Height (m)")
plt.title("Projectile Motion Simulation")
plt.grid(True)

plt.show()