import sys
sys.stdin = open('input.txt')

dij = [(1, 1), (1, -1), (-1, -1), (-1, 1)]


def dfs(i, j, idx, numbers):
    global result

    # 가던 방향 전진
    ni = i + dij[idx][0]
    nj = j + dij[idx][1]

    if 0 <= ni < N and 0 <= nj < N:
        if ni == x and nj == y:
            result = max(result, len(numbers))
            return
        if cafes[ni][nj] not in numbers:
            dfs(ni, nj, idx, numbers + [cafes[ni][nj]])

    # 방향 틀기
    if idx < 3:
        ni = i + dij[idx+1][0]
        nj = j + dij[idx+1][1]

        if 0 <= ni < N and 0 <= nj < N:
            if ni == x and nj == y:
                result = max(result, len(numbers))
                return
            if cafes[ni][nj] not in numbers:
                dfs(ni, nj, idx + 1, numbers + [cafes[ni][nj]])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cafes = [list(input().split()) for _ in range(N)]

    result = -1
    for x in range(N-1):
        for y in range(N-1):
            if cafes[x][y] != cafes[x+1][y+1]:
                dfs(x+1, y+1, 0, [cafes[x][y], cafes[x+1][y+1]])

    print('#{} {}'.format(tc, result))
