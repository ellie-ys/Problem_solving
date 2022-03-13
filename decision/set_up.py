# decision algorithm
# 마구간 정하기.

# 마구간 말 한 마리만 넣을 수 있고, 가장 가까운 두 말의 거리가 최대가 되도록
# c마리의 말가지고 있다.
# 첫 줄에 가장 가까운 두 말의 쵀대 거리
# 가장 가까운 두 말의 거리가 최대가 되도록 하는 그 최대값 출력 프로그램


import sys

input = sys.stdin.readline


n, c = map(int, input().split())
a = []
for _ in range(n):
    a.append(int(input()))


# lt = 0
# rt = max(a)
# # while lt <= rt :
# #     mid = (lt + rt)//2
# #     if 

print(n-c+1)
# 5 3
# 1
# 2
# 8
# 4
# 9
