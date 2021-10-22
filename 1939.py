import sys

input = sys.stdin.readline()
n = int(input)


time = [[0]*2 for _ in range(n)]
for i in range(n):
    s, e = map(int, sys.stdin.readline().split())
    time[i][0] = s
    time[i][1] = e

time.sort(key= lambda x : (x[1], x[0]))

cnt = 1 
end_time = time[0][1]
for i in range(1, n):
    if time[i][0] >= end_time:
        cnt += 1
        end_time = time[i][0]
        
print(cnt)

