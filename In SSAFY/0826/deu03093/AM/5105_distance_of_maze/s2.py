from collections import deque


di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]


def find_start():
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == '2':
                return (i, j)


def bfs(start_i, start_j):
    q = deque()
    cnt = 0
    visited[start_i][start_j] = True
    q.append((start_i, start_j, cnt))

    while q:
        now_i, now_j, cnt = q.popleft()
        if maze[now_i][now_j] == '3':
            return cnt - 1

        for i in range(4):
            next_i, next_j = now_i + di[i], now_j + dj[i]
            if 0 <= next_i < N and 0 <= next_j < N and not visited[next_i][next_j] and maze[next_i][next_j] != '1':
                visited[next_i][next_j] = True
                q.append((next_i, next_j, cnt+1))

    return 0


for T in range(1, 1+int(input())):
    N = int(input())
    maze = [input() for _ in range(N)]
    start_i, start_j = find_start()
    visited = [[False] * N for _ in range(N)]
    ans = bfs(start_i, start_j)
    print('#{} {}'.format(T, ans))
