import sys


def input():
    return sys.stdin.readline().rstrip()


def num(M, N, x, y):
    while x <= M * N:
        if (x - y) % N == 0:
            return x
        x += M
    else:
        return -1

sys.stdin = open('input.txt')
for _ in range(int(input())):
    M, N, x, y = map(int, input().split())
    print(num(M, N, x, y))
