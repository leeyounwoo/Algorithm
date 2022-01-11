import sys
sys.stdin = open('input.txt')

def

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
