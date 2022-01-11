import sys

sys.stdin = open('input.txt')

for T in range(1, int(input()) + 1):
    n, q = map(int, input().split())
    boxs = [0] * (n + 1)

    for i in range(1, q + 1):
        l, r = map(int, input().split())
        for j in range(l, r + 1):
            boxs[j] = i

    print('#{}'.format(T), end=' ')
    for i in range(1, len(boxs)):
        print('{}'.format(boxs[i]), end=' ')
    print()