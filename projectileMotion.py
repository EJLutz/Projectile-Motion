import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

v0 = float(input("Enter the initial velocity (m/s): "))
angle_deg = float(input("Enter the launch angle (degrees): "))
g = 9.81

theta = np.radians(angle_deg)

tFlight = 2 * v0 * np.sin(theta) / g
t = np.linspace(0, tFlight, 100)

x = v0 * np.cos(theta) * t
y = v0 * np.sin(theta) * t - 0.5 * g * t**2
x_final = v0 * np.cos(theta) * tFlight
y_final = v0 * np.sin(theta) * tFlight - 0.5 * g * tFlight**2
y_max = (v0**2) * (np.sin(theta))**2 / (2 * g)

vxFinal = v0 * np.cos(theta)
vyFinal = v0 * np.sin(theta) - g * tFlight
sFinal = math.sqrt(vxFinal**2 + vyFinal**2)

print(f"Total flight time: {tFlight:.3f} s")
print(f"Total Distance: {x_final:.3f} m")


plt.figure(1)
plt.plot(t, y)
plt.plot(0,0,'ro')
plt.plot(tFlight,0,'ro')
plt.plot(.5*tFlight,y_max,'bo')
plt.title("Height vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Vertical Distance (m)")
plt.grid(True)
plt.show()