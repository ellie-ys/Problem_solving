import sys


input = sys.stdin.readline


n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]


a.insert(0, [0]*n)
a.append([0]*n)

for x in a:
    x.insert(0, 0)
    x.append(0)


print(a)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
cnt =0
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt +=1 

print(cnt)

# 5
# 5 3 7 2 3
# 3 7 1 6 1
# 7 2 5 3 4
# 4 3 6 4 1
# 8 7 3 5 2