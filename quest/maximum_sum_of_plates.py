# 격자판 5 *5
#  n * n 격자판이 주어질 때, 각 행의 합, 각 열의 합, 두 대각선의 합 중 가장 큰 합을 출력한다. 


# 첫줄에 자연수 n주어진다. 
import sys


input = sys.stdin.readline


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]



largest = -2147000000

for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        # 행의 값
        sum1 += a[i][j]
        #열의 값
        sum2 += a[j][i]

    if sum1 > largest:
        largest = sum1
    elif sum2 > largest:
        largest = sum2

sum1=sum2=0
for i in range(n):
    # 대각선 가로 합
    sum1 += a[i][i]
    # 대각선 우측위에서 내려오는 합.
    sum2 += a[i][n-i-1]
if sum1> largest:
    largest = sum1
elif sum2 > largest:
    largest = sum2


print(largest)



# 5
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19