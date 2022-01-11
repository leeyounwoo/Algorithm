import sys
sys.stdin = open('input.txt')

# 우하좌상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 터널 구조물
pipe = [
    [],
    [0, 1, 2, 3], # 상하좌우
    [1, 3], # 상하
    [0, 2], # 좌우
    [0, 3], # 상우
    [0, 1], # 하우
    [1, 2], # 하좌
    [2, 3]  # 상좌
]

def DFS(r, c, time):
    visited[r][c] = time
    if time == L: return

    for i in pipe[tunnel[r][c]]:
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < M and tunnel[nr][nc] and ((i+2) % 4 in pipe[tunnel[nr][nc]]) and visited[nr][nc] > time:
            DFS(nr, nc, time+1)

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    # 지도 정보
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    visited = [[987654321] * M for _ in range(N)]   # 방문 체크

    DFS(R, C, 1)

    ans = 0

    for i in range(N):
        for j in range(M):
            if visited[i][j] != 987654321:
                ans += 1

    print('#{} {}'.format(tc, ans))