import sys

sys.stdin = open('input.txt')
n, m = map(int, sys.stdin.readline().split())
see = set()
for _ in range(n):
    see.add(sys.stdin.readline().rstrip())
listen = set()
for _ in range(m):
    listen.add(sys.stdin.readline().rstrip())
see_listen = list(see.intersection(listen))
see_listen.sort()
print(len(see_listen))
for i in see_listen:
    print(i)