import sys
from itertools import combinations
sys.stdin = open('input.txt')

T = int(input())
arr = [i for i in range(1, 13)]

for tc in range(T):
    N, K = map(int, input().split())
    n = len(arr)
    count = 0

    for r in range(n+1):
        for combo in combinations(arr, r):
            if len(combo) == N and sum(combo) == K:
                count += 1
    print("#{} {}".format(tc + 1, count))
