import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()




sys.stdin = open('input.txt')
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    if b not in graph[a]:
        graph[a].append(b)
    if a not in graph[b]:
        graph[b].append(a)
print(graph)
ans = 0
for i in range(1, n+1):
    check = [0] * (n+1)
    bfs(i, n)