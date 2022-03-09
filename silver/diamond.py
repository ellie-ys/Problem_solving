# 격자판 
# n*n 격자판 에서 다이아몬드 모양의 격자판만 수확, 나머지 격자판은 새들을 위해 남겨놓는다.




import sys

input = sys.stdin.readline

n =int(input())
a = [list(map(int, input().split())) for _ in range(n)]

res = 0
# 가로 , 세로
ave = hei = n//2

for i in range(n):
    for j in range(ave, hei+1):
        res += a[i][j]
    if i < n//2:ls
        ave-=1
        hei+=1
    else:
        ave+=1
        hei-=1


print(res)


# 5
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19