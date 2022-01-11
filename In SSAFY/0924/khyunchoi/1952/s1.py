import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    prices = list(map(int, input().split())) # 0: 일, 1: 월, 2: 3달, 3: 연
    months = list(map(int, input().split()))
    min_price = [0] * 12

    min_price[0] = min(prices[0]*months[0], prices[1])
    for i in range(1, 12):
        if i == 1:
            if months[i]:
                min_price[i] = min_price[i-1] + min(prices[0]*months[i], prices[1])
            else:
                min_price[i] = min_price[i-1]
        elif i == 2:
            if months[i]:
                min_price[i] = min(min_price[i-1] + min(prices[0]*months[i], prices[1]), prices[2])
            else:
                min_price[i] = min(min_price[i-1], prices[2])
        else:
            if months[i]:
                min_price[i] = min(min_price[i-1] + min(prices[0]*months[i], prices[1]), min_price[i-3] + prices[2])
            else:
                min_price[i] = min(min_price[i-1], min_price[i-3] + prices[2])

    result = min(min_price[-1], prices[3])
    print('#{} {}'.format(tc, result))
