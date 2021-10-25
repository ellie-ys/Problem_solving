# print the biggest number
# stack : LIFO (Last In First Out)
#입력예제 5276823 3
#출력예제 7823

#입력예제2 977252641 5
#출력예제2    99776

import sys
input = sys.stdin.readline()
num, n = map(int, input.split())
num = list(map(int, str(num)))
stack = []
for x in num:
    while stack and n>0 and stack[-1]<x : #비어있지않고, 
        stack.pop()
        n -= 1
    
    stack.append(x)
if n != 0:
    stack= stack[:-n]

res = ''.join(map(str, stack))
print(res)

# for x in stack:
#    print(x, end ='' )