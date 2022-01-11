import sys
sys.stdin = open('input.txt')

T = int(input())

dy = [0, 1, 0, -1] #오른 아래 왼쪽 위 (행)
dx = [1, 0, -1, 0] # 열
"""
1 2 3 4
12 13 14 5
11 16 15 6
10 9 8 7
"""

for tc in range(1, T+1):
    N = int(input())
    snail = [[0]*N for _ in range(N)] # 달팽이의 크기

    y, x = 0, 0 # 초기값
    dist = 0 # 달팽이가 부딪히지 않게 막아주는 장치(방향전환)

    for n in range(1, N*N + 1): # n이 달팽이의 크기 안에 있을떄
        snail[y][x] = n # 달팽이의 좌표 ex. n = 1 2 3 4    snail[0][0] = n = 1일떄
        y += dy[dist] # 행의 0번쨰니까 0으로 고정 -> 4에 도달할때까지 반복
        x += dx[dist] # 열의 0번쨰니까 1로 쭉 더해주며 오른쪽 전진 ->  반복

        if y < 0 or x < 0 or y >= N or x >= N or snail[y][x] != 0: # 달팽이가 범위를 넘거나 안에 차있는 경우

            # 첫번째 줄의 경우 5에 도착한 경우

            y -= dy[dist] # 하나 뒤로 후퇴
            x -= dx[dist]
            dist = (dist + 1) % 4 # 한바퀴돌아서 부딪히지않도록(ex 1와 12) 혹은 방향 변경하기위해 (4에서 5)
                                    # dict 가 1이 되어서 방향전환 ( 행의 1번째=1 열의 1번째 = 0)
            y += dy[dist]  # 방향을 바꿨으니 하나 더 전진( 밑으로 내려가자)
            # 1로 밑으로 행 하나씩 밑으로 이동 4 5 6 7
            x += dx[dist] # 0으로 열은 고정

    print("#{}".format(tc))
    for i in snail:
        print(*i)
