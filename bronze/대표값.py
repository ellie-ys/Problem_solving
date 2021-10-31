import sys

input = sys.stdin.readline()

n = int(input)
a = list(map(int, input.split()))
ave = (sum(a)//n) + 0.5
ave = int(ave)
#round half even 방식 짝수쪽으로 가는 방식이다
#round half up방식이 아니므로
#0.5를 더해서, int해주어야겠다.
#정수형의 가장 큰 값으로초기화
min = 2147000000

#enumerate() : a라는 리스트, 탐색할때 idx 인덱스값 리턴
for idx, x in enumerate(a):
    #abs 거리구하기.
    tmp=abs(x-ave)
    if tmp < min :
        min = tmp
        score = x
        res = idx+1
    elif tmp == min:
        if x > score:
            score = x
            res = idx+1
print(ave, res)