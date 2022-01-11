# 인접 행렬

import sys
sys.stdin = open('input.txt')

def dfs(v):
    stack = []
    stack.append(v)

    while stack:
        v = stack.pop()
        visited[v] = 1
        if v == end:
            return 1
        for i in range(V + 1):
            if arr[v][i] == 1 and visited[i] == 0:
                stack.append(i)
    return 0
T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    visited = [0 for _ in range(V + 1)]

    arr = [[0 for _ in range(V + 1)] for _ in range(V + 1)]

    for i in range(E):
        a, b = map(int, input().split())
        arr[a][b] = 1
    start, end = map(int, input().split())

    print("#{} {}".format(tc + 1, dfs(start)))

