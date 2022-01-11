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

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    # 지도 정보
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]   # 방문 체크

    Q = [(R, C, 1)]
    visited[R][C] = 1

    ans = 0

    while Q:
        r, c, time = Q.pop(0)
        ans += 1
        if time >= L: continue

        curr_p = tunnel[r][c]

        for i in pipe[curr_p]:
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= M: continue
            if tunnel[nr][nc] == 0 or visited[nr][nc]: continue

            if (i + 2) % 4 in pipe[tunnel[nr][nc]]: # 연결이 되어있는지 확인
                Q.append((nr, nc, time+1))
                visited[nr][nc] = 1

    print('#{} {}'.format(tc, ans))
