import numpy as np
import matplotlib.pyplot as plt
import timestepping as ts
from mpl_toolkits.mplot3d import Axes3D

'''
For this function, b, r, and sigma are the parameters in the Lorenz Equations
initial time t is set to zero and runs to tmax (needs to be a float)
with h being the initial step size
points is a list of initial points at initial t in the form np.array([x, y, z])
with x, y and z being the coordinates
If save set to True, save the final plot as "Lorenz plot.png"
'''


def lorenz_eq(brsigma, tmax, h, points, linearise=False):
    # colours
    colours = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']

    # create 3d figure to plot on
    fig = plt.figure("Lorenz System")
    ax = Axes3D(fig)
    ax.set_title("Lorenz System")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    # first loop goes over each point
    for colour, x in enumerate(points):
        # plot initial points
        ax.scatter(x[0], x[1], x[2])

        # initialise xs, ys and zs arrays
        xs = np.array(x[0])
        ys = np.array(x[1])
        zs = np.array(x[2])

        # initialiase time t
        t = 0
        # times, hs = [], []

        # creates the plot arrays
        while t <= tmax:
            # times.append(t)
            # hs.append(h)
            x = ts.step_rk4(x, h, brsigma, linearise)
            xs = np.append(xs, x[0])
            ys = np.append(ys, x[1])
            zs = np.append(zs, x[2])
            # here put function for generating h
            # h = ts.step_size(x, h, brsigma, ts.step_rk4, 4, 10**-4)
            t += h

        # plot the arrays
        ax.plot(xs, ys, zs, colours[colour], lw=0.5)
        # print(times, hs, len(times), sep='\n')
    return fig