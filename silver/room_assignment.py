

import sys

input = sys.stdin.readline


n = int(input())
meeting = []

for _ in range(n):
    s, e = map(int, input().split())
    meeting.append((s,e)) # tuple형태로 append

#print(meeting)

meeting.sort(key = lambda x : (x[1], x[0]))

#print(meeting)
# 5
# 1 4
# 2 3 
# 3 5 
# 4 6 
# 5 7

end_time = 0
cnt = 0
for s, e in meeting:
    if s >= end_time: #시작하는 시간이 끝나는 시간보다 크거나 같다. 
        # 회의 하나 시작됐으니까...
        # 앤드타임 e가 되는 것
        end_time = e
        cnt+=1
print(cnt)

