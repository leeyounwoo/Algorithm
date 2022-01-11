import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T + 1):
    print('#{}'.format(tc))

    N = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    change = [0] * 8

    for i in range(8):
        if N // money[i] > 0:
            change[i] += N // money[i]
            N = N % money[i]

    print(*change)
