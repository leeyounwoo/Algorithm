import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    if N > M and N >= N+(M // 2)+1:
        result = []
        total = 0
        for i in range(N-(M // 2), N+(M // 2)+1):
            total += numbers[i]
            result.append(total)
        min_result = min(result)
        max_result = max(result)
        fin_result = max_result - min_result
        print('#{} {}'.format(tc, fin_result))

