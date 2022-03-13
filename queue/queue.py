# first in first out

# queue FIFO

# 공주 구하기


import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

dq = list(range(1,n+1))
#print(dq)

dq = deque(dq)

#print(dq)
while dq:
    # 뒤로 넘어가는 사람들
    for _ in range(k-1):
        cur=dq.popleft()
        dq.append(cur) 
    #그냥 사라지는 사람
    dq.popleft()

    if len(dq) == 1:
        print(dq[0])
        dq.popleft() # 여기서 break해도 된다

# 8 3