# organizing storage



# adjust height 

import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())





def Change(num):
    a.sort()
            
    lt = a[0]
    rt = a[-1]

    for _ in range(num):

        a[0] += 1
        a[-1] -= 1
        a.sort()
        print(a)
    return a[-1]-a[0]

print(Change(m))
# 10
# 69 42 68 76 40 87 14 65 76 81
# 50