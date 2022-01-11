from collections import deque
import pprint
import sys
sys.stdin = open('1014/woosteelz/5250_최소비용/sample_input.txt')


dir_x = [0, 1, -1, 0]
dir_y = [1, 0, 0, -1]

for tc in range(int(input())):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [[float('inf') for _ in range(N)] for _ in range(N)]
    visited[0][0] = 0
    queue = deque()
    queue.append([0, 0])

    while queue:
        curr_x, curr_y = queue.popleft()
        for i in range(4):
            next_x, next_y = curr_x + dir_x[i], curr_y + dir_y[i]
            if 0 <= next_x < N and 0 <= next_y < N:
                if graph[next_x][next_y] > graph[curr_x][curr_y]:
                    dist = graph[next_x][next_y] - graph[curr_x][curr_y] + 1
                else:
                    dist = 1

                if visited[next_x][next_y] > visited[curr_x][curr_y] + dist:
                    visited[next_x][next_y] = visited[curr_x][curr_y] + dist
                    queue.append([next_x, next_y])

    print(f'#{tc+1} {visited[N-1][N-1]}')
