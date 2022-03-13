

import sys


input = sys.stdin.readline


num, m = map(int, input().split())

num = list(map(int, str(num)))

stack = []

for x in num:
    while stack and m>0 and stack[-1] <x :
        stack.pop()
        m -= 1
    stack.append(x)

if m != 0:
    stack = stack[:-m]
    
#print(stack)

res = ''.join(map(str, stack))
print(res)


# 5276823 3

# 9977252641 5