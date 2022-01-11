import sys
from itertools import combinations
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [i for i in range(1, 13)]
    n = len(arr)
    result = 0
    for combo in combinations(arr, N):
        if sum(combo) == K:
            result += 1

    print('#{} {}'.format(tc, result))