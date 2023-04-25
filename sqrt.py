
# Python Program to calculate the square root
#https://python.plainenglish.io/4-best-ways-to-find-the-square-root-in-python-4944fda5a876 

#Attempt using built in functions:

#import math
#def find_square(num):
    #result = math.pow(num, 0.5)
    #return result
#square = find_square(float(input("Please enter a number:")) )
#print('Square:',round(square, 1))

import math

def newton(x):
   tolerance = 0.000001
   estimate = 1.0
   while True:
        estimate = (estimate + x / estimate) / 2
        difference = abs(x - estimate ** 2)
        if difference <= tolerance:
            break
   return estimate

def main():
   while True:
       x = input("Please enter a positive number or enter/return to quit: ")
       if x == '':
           break
       x = float(x)
       square_root = newton(x)
       rounded_square_root = round(square_root, 1)
       print(f"The square root of {x} is approx. {rounded_square_root}")
       
main()


