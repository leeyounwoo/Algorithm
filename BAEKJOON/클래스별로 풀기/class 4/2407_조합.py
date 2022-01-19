import sys


def input():
    return sys.stdin.readline().rstrip()


sys.stdin = open('input.txt')
n, m = map(int, input().split())
ans = 1
for i in range(n, n-m, -1):
    ans *= i

for i in range(2, m+1):
    ans //= i

print(ans)