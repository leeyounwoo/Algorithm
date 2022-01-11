import sys

sys.stdin = open('input.txt')

for T in range(1, int(input()) + 1):
    unders = [2, 3, 5, 7, 11]
    ups = [0] * 5
    n = int(input())

    for i in range(len(unders)):
        while True:
            if not n % unders[i]:
                ups[i] += 1
                n //= unders[i]
            else:
                break

    print('#{}'.format(T), end=' ')
    for i in range(len(ups)):
        print('{}'.format(ups[i]), end=' ')
    print()
