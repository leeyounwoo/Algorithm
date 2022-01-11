import sys
sys.stdin = open('input.txt')

T = int(input())

answer = []
for tc in range(1, T+1):

    # 크기를 입력받습니다.
    N = int(input())
    # 다루기 편하게 N을 바꿔줍니다.
    N = N // 10
    # 동적 프로그래밍에 사용할 배열을 정의합니다.
    dp = [0] * (N+1)
    # 시작 값들을 초기화합니다.
    dp[1] = 1
    if N > 1:
        dp[2] = 3
    # 점화식 계산을 수행합니다.
    if N > 2:
        for i in range(3, N+1):
            dp[i] = dp[i-1] + 2*dp[i-2]

    # 결과를 출력합니다.
    result = dp[N]
    answer.append(result)

for tc in range(1, T+1):
    print('#{} {}'.format(tc, answer[tc-1]))
