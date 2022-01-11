import sys
sys.stdin = open('input.txt')


def min_sum(x, y):
    global total, temp
    # 가지치기
    if total < temp:
        return

    # x,y가 목적지에 도달하면 종료
    if x == N - 1 and y == N - 1:
        total += puzzle[x][y]
        # 최소값 갱신하기
        if total > temp:
            total = temp
    # 오른쪽, 아래
    dx, dy = [1, 0], [0, 1]
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            visited[nx][ny] = True
            temp += puzzle[nx][ny]
            min_sum(nx, ny)
            visited[nx][ny] = False
            temp -= puzzle[nx][ny]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    # 최소값
    total = 10**8
    temp = puzzle[0][0]
    # 방문체크
    visited = [[False for _ in range(N)] for i in range(N)]
    # 0,0에서 출발
    min_sum(0, 0)
    print("#{} {}".format(tc, total))
