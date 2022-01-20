import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()


sys.stdin = open('input.txt')
n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parents = {1: 0}
q = deque([1])
while q:
    parent = q.popleft()
    for node in graph[parent]:
        if node not in parents:
            parents[node] = parent
            q.append(node)

for i in range(2, n+1):
    print(parents[i])
