#역수열



import sys

input = sys.stdin.readline

n = int(input())

a = list(map(int,input().split()))

expect = [0]*n
# print(a[0], a[1])
# 1이 들어갈 인덱스! 

for i in range(n):
    if expect[a[i]] == 0:

        expect[a[i]]= i+1
    else :
        expect[a[i]+1] = i+1

print(expect)    
# def Count(idx):
#     a[1:idx]
#     a.sort()
#     return a.index(idx) 


# res = [0]
# for i in range(1,n):
#     res.append(Count(i))

# print(res)


# 8
# 5 3 4 0 2 1 1 0