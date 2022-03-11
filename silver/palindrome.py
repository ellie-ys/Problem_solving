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
cnt = 0 
for i in range(3):
    for j in range(7):
            tmp = a[j][i:i+5]
            print(tmp)
            
            if tmp == tmp[::-1]:
                cnt+=1

for i in range(3):
    for j in range(7):
        tmp2 = a[j][i:i+5]
        print(tmp2)
        if tmp2 == tmp[::-1]:
            cnt +=1

print(cnt)

