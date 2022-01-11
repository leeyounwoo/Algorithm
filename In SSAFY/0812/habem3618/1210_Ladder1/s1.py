import sys
sys.stdin = open('input.txt')

# 뱡향 설정(우 -> 좌 -> 위)
di = [0, 0, -1]
dj = [1, -1, 0]
direction = 2   # 방향의 초기값

for _ in range(1, 11):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 도착점에서 거꾸로 출발하기
    x = 99
    y = ladder[99].index(2)   # 사다리의 마지막 줄에서 2의 위치찾기

    while x > 0:

        new_x = x + di[direction]
        new_y = y + dj[direction]
        # 벽 설정
        if 0 <= new_x < 100 and 0 <= new_y < 100:
            pass

            if ladder[new_x][new_y] == 1:
                x = new_x
                y = new_y
                ladder[new_x][new_y] = 0  # 무한루프? 없애기 위해 지나왔던 길을 없앤다.

        direction = (direction + 1) % 3

    print('#{} {}'.format(tc, y))
