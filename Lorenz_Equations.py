# time steps the Lorenz equations
import numpy as np
import matplotlib.pyplot as pt
import timestepping as ts
from mpl_toolkits.mplot3d import Axes3D

# parameters
b = 8 / 3
r = 28
sigma = 10

# plot the three variables in 3D
fig = pt.figure()
ax = fig.gca(projection='3d')

# time-stepping parameters
tmax = 2.0  # run to this time
nsteps = 100  # number of time steps
dt = tmax / nsteps  # calculate the time step

# initial conditions
t = 0
x1 = np.array([1, 0, 0])
x2 = np.array([0, -1, r - 1])
points = [(x1, 'r'), (x2, 'b')]

# first loop goes over each point
for x, c in points:
    # initialise x, y and z arrays
    xs = np.array(x[0])
    ys = np.array(x[1])
    zs = np.array(x[2])

    n = 0  # number of timesteps taken; initialise to 0

    # creates the plot arrays
    for steps in range(nsteps):
        x = ts.step_rk2(x, dt, b, r, sigma)
        t += dt
        n += 1
        xs = np.append(xs, x[0])
        ys = np.append(ys, x[1])
        zs = np.append(zs, x[2])

        # plot the arrays and initial points
        ax.plot(xs, ys, zs, c, lw=0.1)
    ax.scatter(x[0], x[1], x[2], c)

# show the final image
pt.show()
