#최대공약수와 최소공배수

import sys
input = sys.stdin.readline

A,B = map(int, input().split())
min= 1

def yaksu(Num):
    yak_su = []
    for i in range(1, Num):
        if Num % i == 0:
            yak_su.append(i)
    return yak_su


a = yaksu(A)
b = yaksu(B)
result = [x for x in a if x in b]


def baesu(c,d):
    for j in range(max(c,d), (c*d)+1):
        if j % c == 0 and j% d ==0:
            return j

print(max(result))
print(baesu(A,B))




'''
최대공약수 
서로소가 나올 때까지 계속 공약수로 나누기
최대공약수 공약수만 곱함
최소공배수는 공약수, 서로소까지 곱하기

문제
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

출력
첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.
'''