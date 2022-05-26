# Utkarsh Bajpai @2022
# This program finds fibonacci numbers and uses lru-cache for speed



from functools import lru_cache

#Define the lru-cache decorator over the fibonacci function
@lru_cache
def fibonacci(num):
    if num <=1:
        return num
    else: 
        return fibonacci(num-1) + fibonacci(num-2)


def main():
    i=0
    while(True):
        print(i, fibonacci(i))
        print()
        i+=1
    


if __name__ == '__main__':
    main()