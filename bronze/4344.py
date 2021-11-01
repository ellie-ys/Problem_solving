# 문제
# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.

# 입력
# 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.

# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

T = int(input())
a = []
for i in range(T):
    a = list(map(int, input().split(' ')))

    avag = sum(a[1:]) / (len(a) -1)
    # avag = round(avag, 3)
    # print(avag)
    student_number = 0
    for j in range(1, len(a)):
        
        if a[j]> avag :
            student_number += 1

    # print(student_number)
    percen = (student_number/(len(a) -1))*100
    if len(a) != 101:
        print('{:.3f}%'.format(percen))


#배운점
# 10.0%의ㅣ 소수점 3째짜리까지 출력 
# numpy를 사용하지않는 등
# 잘 풀었다고 생각했는데
# 계속 런타임에러가 났는데 그 이유는
# 첫줄의 FOR I IN RANGE(T) 때문이었다.
# for i in range(T+1)이라고 해서 종료되지않았기 때문이다.