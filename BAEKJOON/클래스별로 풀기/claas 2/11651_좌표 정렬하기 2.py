import sys

n = int(input())
num = []
for _ in range(n):
    num.append(list(map(int, sys.stdin.readline().split())))
num.sort(key=lambda X:[X[1], X[0]])
for i in range(n):
    print('{} {}'.format(num[i][0], num[i][1]))
