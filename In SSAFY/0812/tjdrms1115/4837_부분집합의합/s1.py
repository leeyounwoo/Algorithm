import sys
sys.stdin = open('input.txt')

T = int(input())

answer = []
for tc in range(1, T+1):

    # 1~12를 원소로 갖는 배열을 만듧니다.
    size = 12
    arr = [i+1 for i in range(size)]
    # 원소의 개수 N 및 총합 K를 입력받습니다.
    N, K = map(int, input().split())

    # 원소의 개수가 N이고 총합이 K인 부분집합의 개수를 셉니다.
    result = 0
    for i in range(1 << size):
        total = 0
        count = 0
        for j in range(size):
            if i & (1 << j):
                total += arr[j]
                count += 1
        if count == N and total == K:
            result += 1

    # 결과를 출력합니다.
    answer.append(result)

for tc in range(1, T+1):
    print('#{0} {1}'.format(tc, answer[tc-1]))