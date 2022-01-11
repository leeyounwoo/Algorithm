import sys
sys.stdin = open('input.txt')

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    n = -1
    cnt = 0
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                visited[r][c] = True
                sub_cnt = 1
                sub_n = MAP[r][c]
                # 작은 숫자 찾기
                y, x = r, c
                while True:
                    for d in range(4):
                        ny, nx = y + dy[d], x + dx[d]
                        if 0 <= ny < N and 0 <= nx < N and MAP[ny][nx] == MAP[y][x] - 1:
                            y, x = ny, nx
                            visited[y][x] = True
                            sub_n = MAP[y][x]
                            sub_cnt += 1
                            break
                    else:  # 다음 작은 숫자 없으면 종료
                        break
                # 큰 숫자 찾기
                y, x = r, c
                while True:
                    for d in range(4):
                        ny, nx = y + dy[d], x + dx[d]
                        if 0 <= ny < N and 0 <= nx < N and MAP[ny][nx] == MAP[y][x] + 1:
                            y, x = ny, nx
                            visited[y][x] = True
                            sub_cnt += 1
                            break
                    else:  # 다음 작은 숫자 없으면 종료
                        break
                if sub_cnt > cnt:
                    cnt = sub_cnt
                    n = sub_n
                elif sub_cnt == cnt and sub_n < n:
                    n = sub_n

    print('#{} {} {}'.format(tc, n, cnt))
