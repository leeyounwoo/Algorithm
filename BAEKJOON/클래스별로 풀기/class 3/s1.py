import sys

sys.stdin = open('input.txt')
n, m = map(int, input().split())
# for _ in range(m):
a = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(m)]
for i in range(len(a)):
    print(len(a[i]))