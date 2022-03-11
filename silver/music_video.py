
# 결정 알고리즘 - 범위좁혀나가기
import sys


input = sys.stdin.readline


n, m = map(int, input().split())
a = list(map(int, input().split()))

# print(n, m, a)

# 9 9
# 1 2 3 4 5 6 7 8 9
def Count(mid):
    sum = 0  
    cnt = 1
    for x in a:
        if sum + x > mid:
            cnt+=1 
            sum = x
        else : 
            sum += x
            
    return cnt

        

maxi = 0
for x in a:
    maxi += x
lt = max(a)
print(lt)
rt = maxi
print(maxi)

res = 0
while lt <= rt:
    mid = (lt + rt)//2
    # 최소 m개여야 한다.
    if Count(mid) <= m :
        res = mid
        rt = mid -1
    elif Count(mid)>m:
        lt = mid + 1

print(res)


