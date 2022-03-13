# 

import sys

input = sys.stdin.readline


a = [list(map(int, input().split())) for _ in range(7)]





# 2 4 1 5 3 2 6 
# 3 5 1 8 7 1 7
# 8 3 2 7 1 3 8
# 6 1 2 3 2 1 1
# 1 3 1 3 5 3 2 
# 1 1 2 5 6 5 2
# 1 2 2 2 2 1 5

# 세로 회문은 
# tmp2= a[i:i+5][j]
# 이렇게 작성해서 또 비교해주면 된다고 생각함 
# but out of range 나옴
# 열 slice는 되지만, 행 slice는 이런 방법으로 하지 않는 것으로 판단.
# ->  그냥 비교해주자.
# 
cnt = 0 
for i in range(3):
    for j in range(7):
            tmp = a[j][i:i+5]
            # print(tmp)
            if tmp == tmp[::-1]:
                cnt+=1

            for k in range(2):
                if a[i+k][j] != a[i-k+4][j]:
                    break
            else:    
                cnt+=1



print(cnt)

