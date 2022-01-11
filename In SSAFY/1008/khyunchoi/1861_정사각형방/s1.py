import sys
sys.stdin = open('input2.txt')

dij = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def dfs(i, j):
    global cnt

    for di, dj in dij:
        ni = i + di
        nj = j + dj

        if 0 <= ni < N and 0 <= nj < N:
            if rooms[i][j] + 1 == rooms[ni][nj]:
                cnt += 1
                dfs(ni, nj)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]

    room_num = 0
    result = 0
    for i in range(N):
        for j in range(N):
            cnt = 1
            dfs(i, j)
            if result < cnt:
                result = cnt
                room_num = rooms[i][j]
            elif result == cnt:
                room_num = min(room_num, rooms[i][j])

    print('#{} {} {}'.format(tc, room_num, result))
