'''
# Juan Salcedo
# Plotting linear graphs
# April 26, 2019

# Attempting to use user input instead
# of previously defined linear equation


# Calling necessary libraries
import matplotlib.pyplot as plt
import numpy as np


# Defining x and y
x = np.linspace(-5, 5, 100)
y = 2*x+1

# Calling variables x and y
# Colouring graph "red" and labeling graph
plt.plot(x, y, '-r', label='y=2x+1')

#  Titling plot
plt.title('Graph of y=2x+1')

# Colouring graph in hex
plt.xlabel('x', color='#1C2833')
plt.ylabel('y', color='#1C2833')

# Giving legend
plt.legend(loc='upper left')
plt.grid()

# Calling/showing plot
plt.show()
'''

import numpy as np

# Solving linear equations
A = np.array([[3, -9], [2, 4]])
b = np.array([-42, 2])
z = np.linalg.solve(A, b)
print(z)

M = np.array([[1, -2, -1], [2, 2, -1], [-1, -1, 2]])
c = np.array([6, 1, 1])
y = np.linalg.solve(M, c)
print(y)

# Solving non-linear equations

from scipy.optimize import fsolve

def myFunction(z):
   x = z[0]
   y = z[1]
   w = z[2]

   F = np.empty((3))
   F[0] = x**2+y**2-20
   F[2] = w + 5 - x*y
   return F

zGuess = np.array([1,1,1])
z = fsolve(myFunction,zGuess)
print(z)