import sys
sys.stdin = open('input.txt')

def dfs(x, y, dist):
    global min_dist

    dxy = [(1, 0), (0, 1)]
    
    if dist >= min_dist:
        return

    if x == N-1 and y == N-1:
        min_dist = min(min_dist, dist)

    for dx, dy in dxy:
        nx, ny = x+dx, y+dy

        if nx < N and ny < N and not visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx, ny, dist+arr[nx][ny])
            visited[nx][ny] = 0


T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[0][0] = 1

    min_dist = float('inf')
    dfs(0, 0, arr[0][0])

    print('#{} {}'.format(t, min_dist))