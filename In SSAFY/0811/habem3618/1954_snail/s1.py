import sys
sys.stdin = open('input.txt')

# 시계 방향(오 아 왼 위)
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())

for tc in range(T):
    N = int(input())
    snail = [[0]*N for _ in range(N)]

    # 처음 시작점
    x = y = 0
    # 초기 방향 오른쪽, 아래, 왼쪽, 위쪽
    direction = 0

    for n in range(1, N*N+1):
        snail[x][y] = n   # 처음 시작 (0, 0) = 1
        new_x = x + di[direction]  # 0 + 0 = 0
        new_y = y + dj[direction]  # 0 + 1 = 1

    # 벽 생성
        if 0 <= new_x < N and 0 <= new_y < N and not snail[new_x][new_y]:
            x += di[direction]
            y += dj[direction]

    # 벽을 뚫으면?? 방향 전환
        else:
            direction += 1
            if direction == 4:
                direction = 0
            x += di[direction]
            y += dj[direction]

    print("#{}".format(tc+1))
    for i in snail:
        print(*i)





