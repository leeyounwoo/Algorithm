import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    prices = list(map(int, input().split()))

    result = 0
    current_max = 0
    for i in range(len(prices)-1, -1, -1):
        if current_max < prices[i]:
            current_max = prices[i]
        else:
            result += current_max - prices[i]

    print('#{} {}'.format(tc, result))