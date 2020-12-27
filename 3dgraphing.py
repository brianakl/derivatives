from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from sympy import symbols, diff
import numpy as np
from matplotlib.animation import FuncAnimation

print("This program calculates the gradient on a given point on the z = sin(x) + sin(y) function")
while(True):
    X = float(input("Please enter the x coordinates: "))
    Y = float(input("Please enter the y coordinates: "))
    Z = float(input("Please enter the z coordinates: "))

    point = (np.sin(X) + np.sin(Y))/2
    if (point != Z):
        print("Please enter a point on the surface")
        continue
    fig = plt.figure()

    ax = fig.add_subplot(111,projection='3d')

    x = np.arange(-10, 10, 0.1)
    y = np.arange(-10, 10, 0.1)
    x,y = np.meshgrid(x,y)
    z = (np.sin(x) + np.sin(y))

    surface = ax.plot_surface(x,y,z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    fig.colorbar(surface, shrink=0.5, aspect=5)
    z = x
    #ax.plot_surface(x,y,z, linewidth=0, alpha=0.8, vmin=-10, vmax=10)
    ax.set_zlim(-2,2)

    plt.show()
    inp = input("Would you like to continue?(y/n): ")
    if (inp == "n"):
        break