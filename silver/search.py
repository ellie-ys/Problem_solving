
# 이분검색
# 임의의 수 n개 입력, 오름차순으로 정렬한 다음에 n개의 수 중 한개의 수 m 이 주어지면, 이분검색으로 몇번째에 있는지 구하는 프로그램 작성
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
# print(a)
print(a.index(m)+1)

# 8 32
# 23 87 65 12 57 32 99 81