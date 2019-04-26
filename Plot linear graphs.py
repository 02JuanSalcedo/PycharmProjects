# Juan Salcedo
# Plotting linear graphs
# April 26, 2019

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
