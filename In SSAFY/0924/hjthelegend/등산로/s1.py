import sys
sys.stdin = open('input.txt')

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(x, y, road, skill):
    global answer
    if road > answer:
        answer = road

    visited[x][y] = 1

    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy

        if -1 < nx < n and -1 < ny < n and not visited[nx][ny]:
            # 현 위치보다 낮은곳 이동
            if mountain[nx][ny] < mountain[x][y]:
                dfs(nx, ny, road+1, skill)
            # 높거나 같은 위치로 이동
            elif skill and mountain[x][y] > mountain[nx][ny] - k:
                temp = mountain[nx][ny]
                mountain[nx][ny] = mountain[x][y] - 1
                dfs(nx, ny, road+1, 0)
                mountain[nx][ny] = temp # 원상복구

    visited[x][y] = 0


t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(n)]

    # DFS를 활용하자.
    # 등산로는 가장 높은 봉우리에서 시작.
    max_height = 0
    for i in range(n): # 최대 높이 찾기
        for j in range(n):
            max_height = max(max_height, mountain[i][j])

    visited = [[0] * n for _ in range(n)]
    answer = 0

    for i in range(n):
        for j in range(n):
            if mountain[i][j] == max_height: # 출발점
                dfs(i, j, 1, 1)

    print('#{} {}'.format(tc, answer))