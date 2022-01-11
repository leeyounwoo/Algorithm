import sys
from collections import deque

sys.stdin = open('input.txt')

def bfs(i, j):
    di = [1, 0, 0, -1]
    dj = [0, 1, -1, 0]
    queue = deque([[i, j]])
    visited = [[float('inf')] * N for _ in range(N)]
    visited[i][j] = 0

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            ni = x + di[d]
            nj = y + dj[d]
            if 0 <= ni < N and 0 <= nj < N:
                if visited[ni][nj] > visited[x][y] + path[ni][nj]:
                    visited[ni][nj] = visited[x][y] + path[ni][nj]
                    queue.append([ni, nj])

    return visited[N-1][N-1]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    path = [[int(i) for i in input()] for _ in range(N)]

    print('#{0} {1}'.format(tc, bfs(0, 0)))