# Libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# System parameters
sigma = 5
gamma = 2
threshold = 20.0
inc = 0.01
# Runtime parameters
dt = 0.001
plot_points = 10000

# System
def system(x, y, z):
    dx = y
    dy = sigma*z
    dz = x - gamma*y - z - 2.682E-4*np.sinh(4.0485*x)
    if dz > threshold : dz = threshold
    return dx, dy, dz

# Plotting arrays
x_arr = [0 for i in range(plot_points)]
y_arr = [0 for i in range(plot_points)]
z_arr = [0 for i in range(plot_points)]

# Runtime variables
x = np.random.rand()*4-2
y = np.random.rand()*4-2
z = np.random.rand()*4-2

print(x, y, z)

# Evolve (Euler method) !depreciated

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_zlim(-5, 5)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
trajectory = ax.plot([], [], [], alpha=1.0, linewidth=0.8)[0]

# Text annotation for threshold value
threshold_text = ax.text(-13.0, 6.0, 0.0, '', ha='left', va='top', fontsize=10, color='red')

# Update function
def update(frame):
    global x, y, z, x_arr, y_arr, z_arr, sigma, threshold, inc

    for i in range(2000):
        dx, dy, dz = system(x, y, z)
        x += dx*dt
        y += dy*dt
        z += dz*dt
        x_arr.append(x)
        x_arr.pop(0)
        y_arr.append(y)
        y_arr.pop(0)
        z_arr.append(z)
        z_arr.pop(0)
        
    trajectory.set_data_3d(x_arr, y_arr, z_arr)

    threshold -= inc
    # print(threshold)
    # if threshold<6.5 or threshold>9 : inc = -inc
    # threshold_text.set_text(f'{threshold:.3f}')

    return trajectory, threshold_text

anim = animation.FuncAnimation(fig, update, interval=1, blit=True)
plt.show()
