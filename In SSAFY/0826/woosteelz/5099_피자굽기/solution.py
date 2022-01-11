import sys
sys.stdin = open('input.txt')

TC = int(input())
for tc in range(TC):
    MAXSIZE, M = map(int, input().split())
    temp = list(map(int, input().split()))

    pizza = [(i + 1, temp[i]) for i in range(M)]

    oven = pizza[:MAXSIZE]
    pizza = pizza[MAXSIZE:]

    while not len(oven) == 1:
        idx, left_cheeze = oven.pop(0)
        left_cheeze //= 2
        if left_cheeze:
            oven.append((idx, left_cheeze))
        else:
            if pizza:
                oven.append(pizza.pop(0))

    idx, left_cheeze = oven.pop(0)

    print('#{} {}'.format(tc+1, idx))