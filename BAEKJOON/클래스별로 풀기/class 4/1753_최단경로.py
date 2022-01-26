import sys
import math
from collections import deque

def input():
    return sys.stdin.readline().rstrip()


sys.stdin = open('input.txt')
V, E = map(int, input().split())
k = int(input())
graph = {i: {} for i in range(1, V+1)}
for i in range(E):
    start, end, weight = map(int, input().split())
    if end not in graph[start]:
        graph[start][end] = weight
    elif graph[start][end] > weight:
        graph[start][end] = weight

cost = [math.inf] * (V+1)
cost[k] = 0
q = deque([k])
while q:
    now = q.popleft()
    for next in graph[now].keys():
        print('next', now, next)
        if cost[next] > cost[now] + graph[now][next]:
            cost[next] = cost[now] + graph[now][next]
            q.append(next)

for i in range(1, len(cost)):
    if cost[i] == math.inf:
        print('INF')
    else:
        print(cost[i])
