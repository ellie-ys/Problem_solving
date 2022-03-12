# 증가수열 만들기 그리디 알고리즘


import sys

input =sys.stdin.readline


n = int(input())
a = list(map(int, input().split()))

b = []
letter = []
lt = 0
rt = n-1

while lt <= rt:
    if len(b) == 0:
        if a[lt] < a[rt]:
            b.append(a[lt])
            letter.append("L")
            lt+= 1
        else:
            b.append(a[rt])
            letter.append("R")
            rt -= 1
    else:
        if b[-1] < a[rt]:
            b.append(a[rt])
            letter.append("R")
            rt -= 1
        elif a[lt] > b[-1]:
            b.append(a[lt])
            letter.append("L")
            lt += 1
        else:
            break
        
        # if b[-1] < a[lt]:
        #     b.append(a[lt])
        #     letter.append("L")
        #     lt += 1



print(len(b), end='\n')
for x in letter:
    print(x, end='')
# 5
# 2 4 5 1 3