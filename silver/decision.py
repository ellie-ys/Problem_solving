import sys
# 길이 같은 랜선 만들 때, 길이가 최대가 되어야 한다. 
input = sys.stdin.readline

def Count(len):
    cnt = 0
    for x in a:
        cnt += (x//len)
    return cnt
# 4 11 
# 802
# 743
# 457
# 539
k, n = map(int, input().split())
a = []
res = 0
largest = 0
for _ in range(k):
    tmp = int(input())
    a.append(tmp)
    largest = max(largest, tmp)
lt = 0
rt = largest
while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid) >= n:
        res = mid
        lt = mid + 1
    else: #개수 부족
        rt = mid - 1
print(res)


