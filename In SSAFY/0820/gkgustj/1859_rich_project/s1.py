import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))

    profit =0
    while price:
        max_price = max(price)
        stack = []

        for i in range(len(price)):
            if price[i] == max_price:
                if i == len(price)-1 :
                    price = []
                    break
                price = price[i+1:]
                break
            else:
                stack.append(price[i])

        for _ in range(len(stack)):
            profit += (max_price - stack.pop())

    print('#{} {}'.format(t, profit))