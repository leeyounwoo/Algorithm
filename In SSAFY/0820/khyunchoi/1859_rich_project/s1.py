import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):      # 시간초과
    N = int(input())
    prices = list(map(int, input().split()))

    total = 0
    result = 0
    while len(prices) > 0:
        total = 0
        for i in range(len(prices)):
            total += prices[i]
            if prices[i] == max(prices):
                result += prices[i] * (i + 1) - total
                prices = prices[i + 1:]
                break

    print('#{} {}'.format(tc, result))