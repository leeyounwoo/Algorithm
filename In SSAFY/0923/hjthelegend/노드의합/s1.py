import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
    n, m, l = map(int, input().split())

    for _ in range(m):
        node, number = map(int)