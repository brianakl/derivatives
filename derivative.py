
from pylab import *
from scipy import misc
import numpy as np


ax = subplot()

def fonction(x):
    return 3*x*x*x + 2*x*x+1

x = arange(-2.0, 2.0, 0.01)

y = fonction(x)

yp = misc.derivative(fonction, x)
ypp = misc.derivative(fonction, x,n=2)


grid(True)


plt.plot(x,y, 'r-', label="Original function")
plt.plot(x,yp,'b-', label="Derivitive function")
plt.plot(x,ypp,'g-', label="Second Derivative")
plt.legend(loc="best")
plt.axis(True)
ax.axhline(y=0,color='k')
ax.axvline(x=0,color='k')
show()