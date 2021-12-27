import sys

sys.stdin = open('input.txt')

n, m = sys.stdin.readline().split(" ")
n, m = int(n), int(m)
b = sys.stdin.readline().split(" ")
# print(b)
c = [0, int(b[0])]
for i in range (1, n):
    c.append(c[-1]+int(b[i]))
# print(c)
for _ in range (m):
    x, y = input().split(" ")
    x, y = int(x), int(y)
    print(c[y]-c[x-1])