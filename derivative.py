"""
This is a small program that takes the first and second 
derivatives of a set function and plots it on a graph
"""
from pylab import *
from scipy import misc
import numpy as np


ax = subplot()

#function that is being computed
def func(x):
    return 3 * (x**3) + 2 * (x**2) +1

x = arange(-2.0, 2.0, 0.01)

y = func(x)

yp = misc.derivative(func, x)
ypp = misc.derivative(func, x,n=2)


grid(True)


plt.plot(x,y, 'r-', label="Original function")
plt.plot(x,yp,'b-', label="Derivitive function")
plt.plot(x,ypp,'g-', label="Second Derivative")
plt.legend(loc="best")
plt.axis(True)
ax.axhline(y=0,color='k')
ax.axvline(x=0,color='k')
show()