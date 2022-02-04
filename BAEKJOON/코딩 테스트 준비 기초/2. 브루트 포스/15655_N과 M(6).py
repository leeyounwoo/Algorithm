import sys
from itertools import combinations


def input():
    return sys.stdin.readline().rstrip()


sys.stdin = open('input.txt')
n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
for com in combinations(numbers, m):
    for i in com:
        print(i, end=" ")
    print()