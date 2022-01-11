import sys
sys.stdin = open('input.txt')

from collections import deque


def find_start():
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == '2':
                return (i, j)


di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]


def bfs(start_i, start_j):
    q = deque()
    # 추가하기 전에 True로 바꿈
    visited[start_i][start_j] = True
    q.append((start_i, start_j))

    while q:
        now_i, now_j = q.popleft()
        # 도착지점에 도달한 경우
        if maze[now_i][now_j] == '3':
            return 1

        for k in range(4):
            next_i, next_j = now_i + di[k], now_j + dj[k]
            # 태두리가 1로 둘러싸여 있어서 범위 확인하지 않아도 됌
            if maze[next_i][next_j] != '1' and not visited[next_i][next_j]:
                # 추가하기 전에 True로 바꿈
                visited[next_i][next_j] = True
                q.append((next_i, next_j))

    return 0


for T in range(1, 11):
    tc = int(input())
    maze = [list(input()) for _ in range(16)]
    start_i, start_j = find_start()
    visited = [[False] * 16 for _ in range(16)]
    ans = bfs(start_i, start_j)
    print('#{} {}'.format(T, ans))