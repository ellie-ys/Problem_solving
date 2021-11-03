# 10872번 재귀문제

# 문제
# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.

# 출력
# 첫째 줄에 N!을 출력한다.

# def fact(N):
#     factorial = 1
#     for i in range(1, N+1):
#         factorial *= i
#     return factorial

def fact(N):
    if N <= 0:
        return 1
    else :
        return N * fact(N-1)

N = int(input())
print(fact(N))
    