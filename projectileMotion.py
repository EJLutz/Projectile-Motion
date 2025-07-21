import numpy as np
import matplotlib.pyplot as plt
import math
g = 9.81

def motionCalculations (v0, angle_deg):
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
    return x,y,x_final,y_final,y_max,vxFinal,vyFinal,sFinal,tFlight,t



def plot(t,y,tFlight, y_max):
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

def main():
    v0 = float(input("Enter the initial velocity (m/s): "))
    angle_deg = float(input("Enter the launch angle (degrees): "))
    x, y, x_final, y_final, y_max, vxFinal, vyFinal, sFinal, tFlight, t = motionCalculations(v0, angle_deg)
    print(f"Total flight time: {tFlight:.3f} s")
    print(f"Total Distance: {x_final:.3f} m")
    plot(t, y, tFlight, y_max)
if __name__ == "__main__":
    main()

