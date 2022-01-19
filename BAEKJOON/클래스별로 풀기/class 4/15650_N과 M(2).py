import sys
from itertools import combinations

def input():
    return sys.stdin.readline().rstrip()


sys.stdin = open('input.txt')
n, m = map(int, input().split())
numbers = [i for i in range(1, n+1)]
ans = []
for com in combinations(numbers, m):
    ans.append(com)
for i in range(len(ans)):
    for j in range(m):
        print(ans[i][j], end=' ')
    print()