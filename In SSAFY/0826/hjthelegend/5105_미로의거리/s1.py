import sys
sys.stdin = open('input.txt')
from collections import deque

# 좌 상 우 하
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def maze_runner(x, y):
    queue = deque([])
    queue.append((x, y))
    maze[x][y] = 10 # 다른숫자랑 겹치지않도록 10으로 시작.

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n: # 미로 범위를 벗어났을때 다음으로
                continue

            if maze[nx][ny] == 1: # 벽이라면 다음으로
                continue

            if maze[nx][ny] == 3: # 도착지 만났을때 그 이전꺼 반환하기
                return maze[x][y]

            if maze[nx][ny] == 0: # 통로를 만났을때 표시하기
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

    return 0 # 도착지를 못찾으면 0 반환

t = int(input())
for tc in range(1, t+1):
    n = int(input())

    maze = [list(map(int, input())) for _ in range(n)]

    # 1은 벽 0은 통로, 2에서 출발해 3에 도착해야함.
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2: # 출발점 찾기
                x, y = i, j

    answer = maze_runner(x, y)

    if answer > 0:
        answer = answer - 10 # 다시 원래값으로 돌려주기

    print('#{} {}'.format(tc, answer))