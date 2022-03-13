#역수열



import sys

input = sys.stdin.readline

n = int(input())

a = list(map(int,input().split()))

expect = [0]*n
# print(a[0], a[1])
# 1이 들어갈 인덱스! 
# temp = []
# for i in range(n):
#     temp.append(i+1)

#만약 cnt가 5라면 5인덱스에넣으면 된다.
# 만약 expect에 0이 아니고 숫자가 들어있을경우. 다음칸으로 넘어가줌

print(expect)
print(expect[0:5])

for i in range(2):
    level = expect[0:a[i]].count(0)
    temp = a[i]
    if  level == temp:
        expect[temp] = i+1
    elif temp - level == 1 :
        expect[temp+1] = i+1
    elif temp - level == 2:
        expect[temp+2] = i+1
    

    

print(expect)    
# def Count(idx):
#     a[1:idx]
#     a.sort()
#     return a.index(idx) 


# res = [0]
# for i in range(1,n):
#     res.append(Count(i))

# print(res)


# 8
# 5 3 4 0 2 1 1 0