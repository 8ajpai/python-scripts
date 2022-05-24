

from sympy import fibonacci


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
