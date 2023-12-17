import numpy as np
import matplotlib.pyplot as plt

sigma = 5
gamma = 2
threshold = 20
inc = 0.0001

dt = 0.001
# data_points = 5000

prev_z = 0
x_arr = []
y_arr = []
colmap = []

def system(x, y, z):
    dx = y
    dy = sigma*z
    dz = x - gamma*y - z - 2.682E-4*np.sinh(4.0485*x)
    if dz > threshold : dz = threshold
    return dx, dy, dz

x = np.random.rand()*4-2
y = np.random.rand()*4-2
z = np.random.rand()*4-2

for i in range(1000000):
    dx, dy, dz = system(x, y, z)
    x += dx*dt
    y += dy*dt
    z += dz*dt

while np.linalg.norm([x, y, z]) < 25 :
    dx, dy, dz = system(x, y, z)
    x += dx*dt
    y += dy*dt
    z += dz*dt
    if prev_z < 0 and z > 0 : 
        x_arr.append(x)
        y_arr.append(y)
        colmap.append(threshold/20)
        # data_points -= 1
        threshold -= inc*threshold
        print(f'{threshold:.4f}', end='\r')
    prev_z = z
    
plt.scatter(x_arr, y_arr, c=colmap, s=0.8, cmap='plasma', marker='.', alpha=0.4)

plt.show()