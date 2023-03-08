#$ python squareroot.py
#Please enter a positive number: 14.5
#The square root of 14.5 is approx. 3.8.
# Python Program to calculate the square root
#https://python.plainenglish.io/4-best-ways-to-find-the-square-root-in-python-4944fda5a876 

import math

def find_square(num):
    result = math.pow(num, 0.5)
    return result


square = find_square(float(input("Please enter a number:")) )

print('Square:',round(square, 1))

