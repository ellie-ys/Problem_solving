# 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.

# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

# 출력
# 각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 테스트 케이스 번호는 1부터 시작한다.


import sys

input = sys.stdin.readline
T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    print(f'Case #{i+1}: {A+B}')


# 21 11 02 저녁에
# DFS, BFS 메모리 변화하는 거 그림으로 그리는 거 배운 이후로 
# 간단하지만 메모리 변화하는 모습 그리면서 해봄!
# 완전신기하고 재미있다~