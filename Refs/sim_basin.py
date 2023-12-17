import matplotlib.pyplot as plt
import numpy as np

basin_lims = [(-6.0, 6.0), 
              (-6.0, 6.0)]
num_mesh = 100
mesh = [[0 for i in range(num_mesh)] for j in range(num_mesh)]

max_iters = 2000
max_dist = 15

sigma = 9.3
gamma = 2.0
threshold = 9.0
dt = 0.001

def system(x, y, z):
    dx = y
    dy = sigma*z
    dz = x - gamma*y - z - 2.682E-4*np.sinh(4.0485*x)
    # if dz > threshold : dz = threshold
    return dx, dy, dz

for i in range(num_mesh):
    for j in range(num_mesh):
        print(f'{i}, {j}', end='\r')
        x = basin_lims[0][0] + (basin_lims[0][1] - basin_lims[0][0])*i/num_mesh
        y = basin_lims[1][0] + (basin_lims[1][1] - basin_lims[1][0])*j/num_mesh
        z = 0.0
        for iters in range(max_iters) :
            dx, dy, dz = system(x, y, z)
            x += dx*dt
            y += dy*dt
            z += dz*dt
            if np.linalg.norm([x, y, z])>max_dist :
                mesh[i][j] = max_iters - iters
                break

plt.imshow(mesh, cmap='viridis', interpolation='nearest', extent=[basin_lims[0][0], basin_lims[0][1], basin_lims[1][0], basin_lims[1][1]])
plt.show()