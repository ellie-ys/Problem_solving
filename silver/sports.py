#씨름선수 그리디

# 지원자와 비교하여, 키와 몸무게 중 적어도 하나는 크거나, 무거운 지원자만 뽑기.


import sys
input = sys.stdin.readline

player = []
n = int(input())
for _ in range(n):
    s, e = map(int, input().split())
    player.append((s,e))

        
player.sort(key = lambda x: (x[1], x[0]), reverse =True)
prev_w = 0
prev_h= 0
cnt = n

for h, w in player:
    if h < prev_h  and w < prev_w:
        cnt -= 1
    else:
        prev_h = h
        prev_w = w



        
    
print(cnt)



# 5
# 172 67
# 183 65
# 180 70
# 170 72
# 181 60