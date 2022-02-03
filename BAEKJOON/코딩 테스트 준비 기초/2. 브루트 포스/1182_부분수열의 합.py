import sys
from itertools import combinations


def input():
    return sys.stdin.readline().rstrip()


sys.stdin = open('input.txt')
n, s = map(int, input().split())
numbers = list(map(int, input().split()))

ans = 0
for i in range(1, len(numbers)+1):
    for com in combinations(numbers, i):
        if sum(com) == s:
            ans += 1
print(ans)