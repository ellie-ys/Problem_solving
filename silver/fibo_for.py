import sys

input = sys.stdin.readline

a = int(input())


def fibo(a):

    res1 = 1 # fibo(n-1) 값 저장
    res2 = 1 # fibo(n-2)값 저장

    if a <= 2:
        result = res1
    
    else:
        for i in range(2, a):
            result = res1+ res2   # fibo(n-1)+fibo(n-2)
            res2 = res1
            res1 = result 
        
    return result



print(fibo(a))