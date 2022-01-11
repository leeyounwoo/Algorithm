import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))
    result = []

    for i in range(N-M+1):
        result.append(sum(ai[i:i+M]))

    print('#{} {}'.format(tc+1, max(result) - min(result)))



