#a program that prints a histogram based on:a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, and a plot of the function  h(x)=x3 in the range [0, 10].


import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(5, 2, 1000)

plt.hist(x, bins=50)

def h(x):
    return x**3

x_vals = np.linspace(0, 10, 100)
y_vals = h(x_vals)
plt.plot(x_vals, y_vals, 'r-')

plt.title('Histogram and Function Plot')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.legend()
plt.show()
