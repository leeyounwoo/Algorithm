import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    d, m1, m3, y = map(int, input().split())
    month = [0] + list(map(int, input().split()))

    dp = [0] * 13

    dp[1] = min(m1, month[1] * d)
    dp[2] = dp[1] + min(m1, month[2] * d)

    for i in range(3, 13):
        dp[i] = min(dp[i-3] + m3, dp[i-1] + m1, dp[i-1] + month[i] * d)

    print('#{} {}'.format(tc, min(dp[12], y)))