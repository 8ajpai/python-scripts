

from sympy import fibonacci
#Utkarsh Bajpai @2022
#This program finds Fibonacci numbers. It gets pretty slow around iteration 30 because of poor implementation.
#Check out Fibonacci-cache for a faster version.


#define fibonacci function
def fibonacci(num):
    if num <=1:
        return num

    else:
        return fibonacci(num-1)+fibonacci(num-2)


def main():
    i=0
    while(True):
        print(i, fibonacci(i))
        i+=1
        


if __name__ == '__main__':

    main()
