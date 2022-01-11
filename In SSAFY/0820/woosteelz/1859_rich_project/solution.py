import sys
sys.stdin = open('input.txt')

TC = int(input())
for tc in range(TC):
    ans = 0
    num = int(input())
    profit = list(map(int, input().split()))
    profit.reverse()
    price = profit[0]
    for i in range(num):
        if price < profit[i]:
            price = profit[i]
        else:
            ans += price - profit[i]
    print('#{} {}'.format(tc+1, ans))