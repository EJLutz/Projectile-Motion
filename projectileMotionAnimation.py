import numpy as np
import math
from vpython import *

v0 = float(input("Enter the initial velocity (m/s): "))
angle_deg = float(input("Enter the launch angle (degrees): "))
y_initial = float(input("Enter the initial height (m): "))

# create scene
scene = canvas(title="Projectile Motion Simulation")
ball = sphere(pos=vector(0, y_initial, 0), radius=0.2, color=color.blue, make_trail=True)

g = 9.81
theta = np.radians(angle_deg)
tFlight = (vy := v0 * np.sin(theta)) / g + math.sqrt((vy / g) ** 2 + 2 * y_initial / g) 

vx = v0 * np.cos(theta)
ball.velocity = vector(vx, vy, 0)
x_final = vx * tFlight
y_max = y_initial + (v0**2) * (np.sin(theta))**2 / (2 * g)
print(f"Total flight time: {tFlight:.3f} s")
print(f"Total Distance: {x_final:.3f} m")

t = 0
dt = 0.001

# XY grid
spacing = 1
for x in range(-1, int(x_final) + 2, spacing):
    curve(pos=[vector(x, -1, 0), vector(x, int(y_max) + 2, 0)], color=color.gray(0.7))

for y in range(-1, int(y_max) + 2, spacing):
    curve(pos=[vector(-1, y, 0), vector(int(x_final) + 2, y, 0)], color=color.gray(0.7))

# axes
curve(pos=[vector(-1, 0, 0), vector(x_final + 1, 0, 0)], color=color.red)  # X-axis
curve(pos=[vector(0, -1, 0), vector(0, y_max + 1, 0)], color=color.green)  # Y-axis

while ball.pos.y >= 0:
    rate(100)
    ball.velocity.y -= g * dt
    ball.pos += ball.velocity * dt
    t += dt