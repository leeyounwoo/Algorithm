import sys
sys.stdin = open('input.txt')
from collections import deque

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# 다익스트라 알고리즘

def dijkstra():
    visited = [[100435262362351 for _ in range(n)] for _ in range(n)]
    queue = deque([(0, 0)])
    visited[0][0] = 0
    while queue:
        x, y = queue.popleft()
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if -1 < nx < n and -1 < ny < n:
                count = 0
                # 높이차이만큼 추가연료 소비
                if arr[x][y] < arr[nx][ny]:
                    count = arr[nx][ny] - arr[x][y]

                # 거리 update
                if visited[nx][ny] > visited[x][y] + count + 1: # not visited
                    visited[nx][ny] = visited[x][y] + count + 1
                    queue.append((nx, ny))

    return visited[n-1][n-1]

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # 높이 차이만큼 추가 연료 소비
    answer = dijkstra()
    print('#{} {}'.format(tc, answer))