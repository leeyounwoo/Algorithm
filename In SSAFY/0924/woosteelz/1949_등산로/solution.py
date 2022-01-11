import sys
from collections import deque
sys.stdin = open('0924/woosteelz/1949_등산로/input.txt')

for tc in range(int(input())):
    n, k = map(int, input().split())
    graph = [list(map(int, input())) for _ in range(n)]
    visited = [[0 for _ in range(n)] for _ in range(n)]
    dir_x = [0, 1, 0, -1]
    dir_y = [1, 0, -1, 0]

    queue = deque()

    max_height = max(map(max, graph))
    for i in range(n):
        for j in range(n):
            if graph[i][j] == max_height:
                queue.append([i, j])
                visited[i][j] = 1

    while queue:
        curr_x, curr_y = queue.popleft()
        for i in range(4):
            next_x = curr_x + dir_x[i]
            next_y = curr_y + dir_y[i]
            if 0 <= next_x < n and 0 <= next_y < n:
                if graph[curr_x][curr_y] > graph[next_x][next_y] and not visited[next_x][next_y]:
                    pass
                if graph[curr_x][curr_y] > graph[next_x][next_y] - k and not visited[next_x][next_y]:
                    pass
