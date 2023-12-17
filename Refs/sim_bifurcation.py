import numpy as np
import matplotlib.pyplot as plt

sigma = 9
gamma = 2
threshold = 9.5
inc = 0.001

dt = 0.001
data_points = 50

iteration = 0
prev_dz = 0
bifurcation = []
threshold_arr = []
lyapunov_coeff = []
lyapunov_threshold = []
lpnvsum = 0

def system(x, y, z):
    dx = y
    dy = sigma*z
    dz = x - gamma*y - z - 2.682E-4*np.sinh(4.0485*x)
    if dz > threshold : dz = threshold
    return dx, dy, dz

x = np.random.rand()*4-2
y = np.random.rand()*4-2
z = np.random.rand()*4-2

for i in range(100000):
    dx, dy, dz = system(x, y, z)
    x += dx*dt
    y += dy*dt
    z += dz*dt

fig, axs = plt.subplots(2, 1, sharex=True)
axs[0].set_ylabel('Bifurcation')
axs[1].set_ylabel('Lyapunov coefficient')
axs[1].set_xlabel('Threshold')
axs[1].set_ylim(-1, 6)


while threshold > 6.40 :
    dx, dy, dz = system(x, y, z)
    x += dx*dt
    y += dy*dt
    z += dz*dt
    if prev_dz < 0 and dz > 0 : 
        bifurcation.append(y)
        threshold_arr.append(threshold)
        lpnvsum += np.log(np.abs(dy))
        iteration += 1
    if iteration>data_points : 
        iteration = 0
        lyapunov_coeff.append(lpnvsum/data_points)
        lyapunov_threshold.append(threshold)
        lpnvsum = 0
        threshold -= inc
        print(f'{threshold:.2f}', end='\r')
    prev_dz = dz
    
axs[0].scatter(threshold_arr, bifurcation, s=1.0, c='blue', marker='.', alpha=0.5)
axs[1].scatter(lyapunov_threshold, lyapunov_coeff, s=1.0, c='blue', marker='.', alpha=0.5)


iteration = 0
prev_dz = 0
bifurcation = []
threshold_arr = []
lyapunov_coeff = []
lyapunov_threshold = []
lpnvsum = 0

while threshold < 9.50 :
    dx, dy, dz = system(x, y, z)
    x += dx*dt
    y += dy*dt
    z += dz*dt
    if prev_dz < 0 and dz > 0 : 
        bifurcation.append(y)
        threshold_arr.append(threshold)
        lpnvsum += np.log(np.abs(dy))
        iteration += 1
    if iteration>data_points : 
        iteration = 0
        lyapunov_coeff.append(lpnvsum/data_points)
        lyapunov_threshold.append(threshold)
        lpnvsum = 0
        threshold += inc
        print(f'{threshold:.2f}', end='\r')
    prev_dz = dz

axs[0].scatter(threshold_arr, bifurcation, s=1.0, c='red', marker='.', alpha=0.5)
axs[1].scatter(lyapunov_threshold, lyapunov_coeff, s=1.0, c='red', marker='.', alpha=0.5)

plt.show()