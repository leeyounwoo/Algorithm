import sys

sys.stdin = open('input.txt')
for _ in range(int(input())):
    n = int(input())
    d = [0, 1, 1, 1]
    for i in range(4, n+1):
        d.append(d[i-3] + d[i-2])
    print(d[n])