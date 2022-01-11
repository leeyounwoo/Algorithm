import sys
from itertools import combinations
sys.stdin = open('input.txt')

for T in range(1, int(input()) + 1):
    ele_count, ele_sum = map(int, input().split())
    arr = [i for i in range(1, 13)]
    n = len(arr)

    ans = 0
    for combo in combinations(arr, ele_count):
        if sum(combo) == ele_sum:
            ans += 1

    print('#{} {}'.format(T, ans))