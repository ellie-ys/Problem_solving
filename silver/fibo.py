import sys

input = sys.stdin.readline

x = int(input())

def fibo(n):
    for i in range(n):
        if n>2:
            return fibo(n-1) + fibo(n-2)    
        else:
            return 1



print(fibo(x))

# fibonacci  알고리즘, 재귀 알고리즘을 적용했지만
# 그것보다 직접 for 이나  while을 사용하는 게 더 빠르고 효율적이다.

# recursive재귀 미학에 초점을 맞추느라 효율성을 희생 시켰다면
# 다음번엔 for loop를 사용해서 최적화를 해보자.

