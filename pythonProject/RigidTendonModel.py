# This is simple practice project for simulating muscle force using the Rigid-Tendon model explained in the following paper:
# Millard M, Uchida T, Seth A, Delp SL. Flexing computational muscle: modeling and simulation of musculotendon dynamics. J Biomech Eng. 2013 Feb;135(2):021005. doi: 10.1115/1.4023390. PMID: 23445050; PMCID: PMC3705831.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#--------------- Muscle Parameters ---------------
OptimalFiberLength = 1  
MaximumForce = 1500  
alpha_opt = np.radians(10)  
TendonLength = 0.2 
Vel_contraction_max = 10.0  
b = 0.1  
activation = 0.5  
MuscleLength = 1.2
MuscleVel = 0.0

#--------------- Simulation Parameters ---------------
dt = 0.01 
total_time = 5.0  
steps = int(total_time / dt)  
link_length = 0.5  
theta = np.pi / 10
omega = 0.0  
inertia = 20.0  
joint_d = 0.1 
theta_min = 0  
theta_max = 4*np.pi / 9  

time_history = np.zeros(steps)
theta_history = np.zeros(steps)
omega_history = np.zeros(steps)
force_history = np.zeros(steps)
MuscleLength_history = np.zeros(steps)


#--------------- Function Definitions ---------------
def force_velocity_relationship(v_m):
    if v_m < 0:
        return (1.4 - 0.4 * (v_m / Vel_contraction_max))
    else:
        return (1 - v_m / Vel_contraction_max) / (1 + v_m / (0.4 * Vel_contraction_max))

def ComputeMuscleForce(MuscleLength, MuscleVel, activation):
    l_m = max(OptimalFiberLength * np.cos(alpha_opt), MuscleLength - TendonLength)
    return MaximumForce * (activation * max(0.0, 1.0 - ((l_m - OptimalFiberLength) / OptimalFiberLength) ** 2) * force_velocity_relationship(MuscleVel) + b * MuscleVel) * np.cos(alpha_opt)


# Simulation
def Simulate(dt):
    global MuscleLength, MuscleVel, activation, theta, omega

    for i in range(steps):
        # Compute muscle force
        muscle_force = ComputeMuscleForce(MuscleLength, MuscleVel, activation)
        muscle_torque = muscle_force * link_length / 2
        gravity_torque = -9.83 * inertia * link_length**2 * np.cos(theta)
        torque = muscle_torque + gravity_torque
        print(f'muscle force: {muscle_force}, muscle torque: {muscle_torque}, gravity torque: {gravity_torque}')
    
        # Solve Newton-Euler
        alpha = (torque - joint_d * omega) / inertia
        omega += alpha * dt
        theta += omega * dt
    
        # Constraints
        if theta > theta_max:
            theta = theta_max
            omega = 0
    
        elif theta < theta_min:
            theta = theta_min
            omega = 0
    
        MuscleLength += -0.005 * omega  # Update muscle length
    
        if (i > steps / 10):
            activation = 0
    
        # Data log
        time_history[i] = i * dt
        theta_history[i] = theta
        omega_history[i] = omega
        force_history[i] = muscle_force
        MuscleLength_history[i] = MuscleLength

# Plotting
def PlotDiagrams():
    plt.figure(1)
    plt.subplot(4, 1, 1)
    plt.plot(time_history, theta_history)
    plt.title('Position - Time')
    plt.ylabel('Angle (rad)')
    
    plt.subplot(4, 1, 2)
    plt.plot(time_history, omega_history)
    plt.title('Angular Velocity - Time')
    plt.ylabel('Angular Velocity (rad/s)')
    
    plt.subplot(4, 1, 3)
    plt.plot(time_history, force_history)
    plt.title('Muscle Force - Time')
    plt.ylabel('Force (N)')
    
    plt.subplot(4, 1, 4)
    plt.plot(time_history, MuscleLength_history)
    plt.title('Muscle-Tendon Length - Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Length (m)')
    
    plt.tight_layout()
    plt.show()

# Visualization
def plot_links_and_muscle(theta, MuscleLength, link_length=1.0):
    x0, y0 = 0, 0
    x1, y1 = link_length, 0
    x2 = x1 + link_length * np.cos(theta)
    y2 = y1 + link_length * np.sin(theta)
    xm = x1 + (link_length / 2) * np.cos(theta)
    ym = y1 + (link_length / 2) * np.sin(theta)

    # Plot links
    plt.plot([x0, x1], [y0, y1], 'k-', lw=3)
    plt.plot([x1, x2], [y1, y2], 'r-', marker='o', markersize=8, lw=3)
    plt.plot([x0, xm], [y0, ym], 'b--', lw=2)

    plt.xlim(-2 * link_length, 2 * link_length)
    plt.ylim(-2 * link_length, 2 * link_length)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title('Muscle Connected to Middle of Second Link Animation')
    plt.xlabel('X (m)')
    plt.ylabel('Y (m)')

# Main
def main():
    Simulate(dt)
    PlotDiagrams()
    # Animation
    fig, ax = plt.subplots()

    def update(frame):
        ax.clear()
        plot_links_and_muscle(theta_history[frame], MuscleLength_history[frame])

    ani = FuncAnimation(fig, update, frames=steps, interval=dt * 1000, repeat=False)
    plt.show()

if __name__ == "__main__":
    main()