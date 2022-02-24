import sys


def input():
    return sys.stdin.readline().rstrip()


sys.stdin = open('input.txt')
n = int(input())
ans = 0
for i in range(1, n+1):
    ans += (n // i) * i
print(ans)