import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    n = N // 10 # 규칙을 실행할 횟수

    result = 1 # N이 10일때는 1이므로 여기에서부터 시작
    if N == 10: # N이 10이면 그대로 결과값 출력
        pass
    else:
        i = 0
        # N: 10 result: 1
        # N: 20 result: 3 이전 숫자에서 * 2 + 1
        # N: 30 result: 5 이전 숫자에서 * 2 - 1
        # N: 40 result: 11 이전 숫자에서 * 2 + 1
        # N: 50 result: 21 .....
        # N: 60 result: 43 .....
        # N: 70 result: 85 .....
        while i < n - 1: # 규칙을 그대로 실행
            if i % 2:
                result = result * 2 - 1
                i += 1
            else:
                result = result * 2 + 1
                i += 1

    print('#{0} {1}'.format(tc, result))