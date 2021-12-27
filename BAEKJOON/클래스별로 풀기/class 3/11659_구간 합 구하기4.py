import sys

sys.stdin = open('input.txt')
n, t = map(int, sys.stdin.readline().rstrip().split())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
d = [0]
for i in range(1, n+1):
    d.append(d[i-1] + numbers[i-1])
for _ in range(t):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    print(d[j] - d[i-1])