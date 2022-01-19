import sys
from itertools import combinations_with_replacement

def input():
    return sys.stdin.readline().rstrip()


sys.stdin = open('input.txt')
n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
ans = []
for com in combinations_with_replacement(numbers, m):
    ans.append(com)
for i in range(len(ans)):
    for j in range(m):
        print(ans[i][j], end=' ')
    print()