import sys
sys.stdin = open('input.txt')

T = int(input())
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
for tc in range(T):
    N = int(input())
    snail = [[0]*N for _ in range(N)]
    x, y = 0, 0                        # 초기 위치
    dir_stat = 0                       # 초기 방향 오른쪽

    for n in range(1, N*N+1):
        snail[x][y] = n
        x = x + dx[dir_stat]           # 내가 바로 다음으로 갈 위치
        y = y + dy[dir_stat]
        if x >= N or y >= N or x < 0 or y < 0 or snail[x][y] != 0:
            x -= dx[dir_stat]
            y -= dy[dir_stat]
            dir_stat = (dir_stat+1) % 4
            x = x + dx[dir_stat]
            y = y + dy[dir_stat]
    for i in snail:
        print(*i)



