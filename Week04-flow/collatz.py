#from ast import While
#num = int(input("Enter a number:"))
#while num == 1: 
    #if (num % 2) == 0:
        #print (f"{num/2}")
    #else:
        #print (f"{num * 3 + 1}")
#https://stackoverflow.com/questions/63795905/building-a-function-to-return-integer-until-reaching-1-in-python


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
