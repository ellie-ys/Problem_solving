
# 타이타닉 
# 보트 한 개 탈 수  ㅇ는 총  무도 m 이하로 제한되어 있다,
# 구명 보트는 2명 이하로만 탈 수 있다.
# n명의 승객 몸무게가주어졌을 때 승객 모두가 탈출하기 위한 구명보트의 최소 개수 출력!

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

a = list(map(int, input().split()))


# print(n,m, a)


# 5 140
# 90 50 70 100 60

a.sort()
lt = 0
rt = n-1
cnt =0

while lt <=  rt :

    for i in range((n//2)+1):

        if a[lt]+a[rt] <= m :
            cnt+=1
            lt +=1
            rt-=1
        elif a[lt]+a[rt] > m:
            cnt+=1
            rt -=1
            
print(cnt)
