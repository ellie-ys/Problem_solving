# 곶감, 모래시계 


import sys

input= sys.stdin.readline

n = int(input()) # n*n 격자판
a = [list(map(int, input().split())) for _ in range(n)]
# print(a)
m = int(input()) # 회전명령 개수

for _ in range(m):
    avenue, direct, num = map(int, input().split())

    if direct == 0: 
        #left
        for _ in range(num):
            a[avenue-1].append(a[avenue-1].pop(0))
            # pop(0) 맨 앞꺼 pop
    elif direct ==1:
            # right
        for _ in range(num):
            a[avenue-1].insert(0, a[avenue-1].pop())


print(a)


# 5
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19
# 3
# 2 0 3
# 5 1 2
# 3 1 4

# 모래시계 모양의 합 구하기

res = 0

s = 0
e = n-1
for i in range(n):

    for j in range(s, e+1):
        res += a[i][j]
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -=1
        e +=1

print(res)


