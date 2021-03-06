
#  응급실 
#위험도가 같은 것이 들어갈 수 있기 때문에 그냥 오름차순 정렬로는 안됨.
# 
# 병원 응급실엔 의사가 한 명밖에 없다.

import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int, input().split())

Q =[(pos, val ) for pos, val in enumerate(list(map(int, input().split())))]

Q = deque(Q)
cnt = 0
while True:

    cur = Q.popleft()
    if any(cur[1] > x[1] for x in Q):
        Q.append(cur)
    else:
        cnt+=1
        if cur[0] == m:
            print(cnt)
            break 

# 5 2
# 60 50 70 80 90

# [응급실(큐)]

# 메디컬 병원 응급실에는 의사가 한 명뿐이다.


# 응급실은 환자가 도착한 순서대로 진료를하며, 위험도가 높은 환자는 빨리 응급조치를 해야한다. 이러한 문제를 해결하기 위해 응급실은 다음과 같은 방법으로 환자의 진료순서를 정한다.



# 응급실에 접수한 순서대로 환자의 진료를 본다.
# 단, 해당 순서의 환자보다 위험도가 높은 환자가 존재하면 그 환자는 대기목록의 맨 마지막으로 보내진다.
# 만약, 해당 순서의 환자보다 위험도가 높은 환자가 없으면 그 환자를 진료한다.
 

# 현재 N명의 환자가 응급실의 대기목록에 있으며, 대기목록에는 환자의 위험도가 함께 표시되어 있다.

# 대기 목록상의 M번째 환자가 몇 번째로 진료를 받는지 출력하는 프로그램을 작성하시오.

# (단, 대기 목록상의 M번째는 대기목록의 첫 번째 환자를 0번째로 간주하여 표기한 것임)



# *입력 설명

# 첫 번째 줄에 자연수 N(5 ≤ N ≤ 100)과 M(0 ≤ M < N)이 주어진다.

# 두 번째 줄에 접수한 순서대로 환자의 위험도(50 ≤ 위험도 ≤ 100)가 주어진다.

# 위험도는 값이 높을수록 더 위험하다는 뜻이며, 위험도가 같은 환자가 존재할 수 있다.


# *출력 설명

# M번째 환자가 몇 번째로 진료 받는지를 출력한다.