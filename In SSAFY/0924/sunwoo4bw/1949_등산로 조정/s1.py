import sys
sys.stdin = open('input.txt')

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs (r, c, road, skill):
    global ans
    if road > ans :
        ans = road
    visited[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc <N and not visited[nr][nc]:
            # 낮은 곳으로 이동
            if mt[r][c] > mt[nr][nc]:
                dfs(nr, nc, road+1, skill)
            # 높거나 같은 곳으로 이동
            elif skill and mt[r][c] > mt[nr][nc] - K:
                tmp = mt[nr][nc]
                mt[nr][nc] = mt[r][c] -1
                dfs(nr, nc, road+1, 0) # 스킬 사용
                mt[nr][nc] = tmp # 원상복구
    visited[r][c] = 0

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split()) # N: 한변의 길이, K: 최대 공사가 가능한 깊이(딱 한 곳만 dig)
    mt = [list(map(int, input().split())) for _ in range(N)]
    # [[9, 3, 2, 3, 2], [6, 3, 1, 7, 5], [3, 4, 8, 9, 9], [2, 3, 7, 7, 7], [7, 6, 5, 5, 8]]

    # 가장 높은 봉우리 찾기
    max_h = 0
    for i in range(N):
        for j in range(N):
            if max_h < mt[i][j]:
                max_h = mt[i][j]

    # 어느 방향으로 깎을지 정해야지/ 4방향만 신경쓰면 돼
    # 중복을 막아야 해서 visited 체크
    visited = [[0] * N for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            if mt[i][j] == max_h:
                dfs(i, j, 1, 1)

    print('#{} {}'.format(tc, ans))

