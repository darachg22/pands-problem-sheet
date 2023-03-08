
# Python Program to calculate the square root
#https://python.plainenglish.io/4-best-ways-to-find-the-square-root-in-python-4944fda5a876 
import math

def find_square(num):
    result = math.pow(num, 0.5)
    return result


square = find_square(int(input("Please enter a number:")) )

print('Square:',square)
