# 쇠막대기


#레이저 쇠막대기

import sys

input = sys.stdin.readline

s = input()
stack =[]
sum = 0


for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
        # print(stack)
    else:
        #closed bracket
        if s[i-1] == '(':
            # raser
            stack.pop()
            # print(stack)
            sum += len(stack)
            
        else:
            stack.pop()
            # print(stack)
            sum+=1
            

print(sum)




#()(((()())(()())))(())