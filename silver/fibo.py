import sys

input = sys.stdin.readline

x = int(input())

def fibo(n):
    for i in range(n):
        if n>2:
            return fibo(n-1) + fibo(n-2)    
        else:
            if n <= 2:
                return 1



print(fibo(x))