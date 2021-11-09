'''
문제
자연수 N이 주어진다. N을 이진수로 바꿔서 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N이 주어진다. (1 ≤ N ≤ 100,000,000,000,000)

출력
N을 이진수로 바꿔서 출력한다. 이진수는 0으로 시작하면 안 된다.

예제 입력 1 
53
예제 출력 1 
110101
'''
N = int(input())

Binary = []
def recur(num):
    
    if num == 1:
        Binary.append(1)
    elif num // 2 == 0:
        Binary.append(0)
        Binary.append(num%2)
    else:
        Binary.append(num%2)
        recur(num//2)

recur(N)
for _ in range(len(Binary)):
    print(Binary.pop(), end='')