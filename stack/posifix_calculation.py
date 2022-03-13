# 후위 연산


import sys

input = sys.stdin.readline

a = input()

# 풀이 예상

# 스택만나면 무조건 stack에 push ..!! 
# 만약 연산자 만나면, 앞의 2개 꺼내서 계산! 

# 나중에 나오는 게, 뒤로 가서 연산해야함.
stack = []
res = 0
temp1 = temp2 = temp = 0
for x in a :
    if x.isdecimal():
        stack.append(int(x))
    else:
        if x =='+':
            temp2 = stack.pop()
            temp1 = stack.pop()
            temp = temp1 + temp2
            stack.append(temp)
        elif x =='-':
            temp2 = stack.pop()
            temp1 = stack.pop()
            temp = temp1 - temp2
            stack.append(temp)
        elif x =='*':
            temp2 = stack.pop()
            temp1 = stack.pop()
            temp = temp1 * temp2
            stack.append(temp)
        elif x == '/':
            temp2 = stack.pop()
            temp1 = stack.pop()
            temp = temp1/temp2
            stack.append(temp)


print(stack[0])

# 352+*9-
