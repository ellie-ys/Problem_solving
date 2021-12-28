# 숫자아규


import sys
import itertools

input = sys.stdin.readline


# 민혁이가 영수에게 질문한 횟수 T
# 영수가 생각하고 있는 답의 총 개수
data = []
N = int(input())
for _ in range(N):
    num, s, b = map(int, input().split())
    data.append([num, s, b])



def check(case, number):
    strike = 0
    ball = 0
    num, s, b = case
    for idx, digit in enumerate(number):
        for idx_case, digit_case in enumerate(str(num)):
            if digit == digit_case:
                if idx == idx_case:
                    strike += 1
                else:
                    ball += 1

    if s == strike and b == ball:
        return True
    else:
        return False

result = []
nPr = list(itertools.permutations(['1','2','3','4','5','6','7','8','9'], 3))

for number in nPr:
    possible = True
    for case in data:
        possible = check(case, number)
        if possible == False:
            break
    if possible == True:
        result.append(number)

print(len(result))
#  1개 -> 123, 356 중에 공통되는 숫자 1개 영수가 생각하는 숫자

# strike가 2개 -> 3, 2, 7 중에 2개가 영수가 생각하는 숫자

# strike가 0개 -> 영수가 생각하는 숫자 없음





