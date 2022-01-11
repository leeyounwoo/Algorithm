import sys
sys.stdin = open('input.txt')

dy = [-1,1,1,-1]
dx = [1,1,-1,-1]

def dfs(y, x, cnt, index, turned):
    global result, yy, xx
    if turned > 4:
        return
    if y == yy and x == xx and cnt != 0:
        if result < cnt:
            result = cnt
        return
    if info[y][x] in visited_numbers:
        return

    cnt += 1
    visited_numbers.append(info[y][x])

    if cnt == 1:
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<= nx < N and 0<= ny < N:
                dfs(ny,nx,cnt, i, turned)
    else:
        ny = y + dy[index]
        nx = x + dx[index]
        if 0 <= nx < N and 0 <= ny < N:
            dfs(ny, nx, cnt, index, turned)
        index = (index+1) % 4
        ny = y + dy[index]
        nx = x + dx[index]
        if 0 <= nx < N and 0 <= ny < N:
            dfs(ny, nx, cnt, index, turned+1)
    visited_numbers.pop()

T = int(input())
for tc in range(T):
    N = int(input())
    info = [list(map(int, input().split())) for _ in range(N)]
    visited_numbers = []
    result = -1
    for i in range(N):
        for j in range(N):
            yy = i
            xx = j
            dfs(i,j, 0, 0, 0)

    print('#{} {}'.format(tc+1, result))