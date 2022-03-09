# 수들의 합
# 이 수열의 i번째~ j번째 수 까지 합 이 m이 되는 경우의 수 구하기. 

import sys


input = sys.stdin.readline


n, m = map(int, input().split())

a = list(map(int, input().split()))

  
# 8 3
# 1 2 1 3 1 1 1 2


left = 0
right = 1
cnt = 0
tot = a[0]


while True:
    if tot < m :
        if right < n:
            tot += a[right]
            right +=1
        else:
            break
    elif tot == m :
        cnt +=1
        tot -=a[left]
        left += 1
    else:
        tot -= a[left]
        left +=1


print(cnt)
