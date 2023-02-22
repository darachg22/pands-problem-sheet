#Author: Darach Gorham

#asks the user to input any positive integer and outputs the successive values of the following calculation:
#At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.

#First attempt using no outside research:

#from ast import While
#num = int(input("Enter a number:"))
#while num == 1: 
    #if (num % 2) == 0:
        #print (f"{num/2}")
    #else:
        #print (f"{num * 3 + 1}")
#Resource used to help finish assignment: https://stackoverflow.com/questions/63795905/building-a-function-to-return-integer-until-reaching-1-in-python


def Collatz(n):

    out=[n]
    while n>1:
        if n%2==0:
            n = n/2
        else:
            n = (n*3)+1
        out.append(int(n))
    return out

print(Collatz(int(input("Enter a number:"))))
