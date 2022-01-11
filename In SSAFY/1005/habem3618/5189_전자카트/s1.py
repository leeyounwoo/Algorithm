import sys
sys.stdin = open('input.txt')
from itertools import permutations


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    perm = permutations([i for i in range(1, N)])

    total = 10**8

    for i in perm:
        temp = 0
        x = 0
        for j in i:
            temp += puzzle[x][j]
            x = j
        temp += puzzle[x][0]

        if total > temp:
            total = temp

    print("#{} {}".format(tc, total))
