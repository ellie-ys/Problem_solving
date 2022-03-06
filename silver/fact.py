

import sys

input = sys.stdin.readline
x = int(input())




#반복적으로 구현

# def fact(n):
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#     return result



# 재귀적으로 구ㄴ
def fact(n):
    if n<= 1:
        return 1
    return n*fact(n-1)

print(fact(x))

