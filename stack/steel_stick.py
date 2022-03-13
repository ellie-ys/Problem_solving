# 쇠막대기 레이저 쇠막대기
# 괄호가 '(' or ')'인데, if- else 문을 사용하면 
# pop from empty list 라는 에러가 나온다. 왜 그럴까?


import sys

input = sys.stdin.readline

s = input()
stack =[]
sum = 0


for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
        # print(stack)
    elif s[i] == ')':
        #closed bracket
        stack.pop()
        if s[i-1] == '(':
            # raser 컷팅! 지금까지 스택의 길이를 더해준다.
            sum += len(stack)
            
        elif s[i-1] == ')':
            # stick 길이기 때문
            sum+=1
            

print(sum)




# ()(((()())(())()))(())
