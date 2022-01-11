import sys
sys.stdin = open('input.txt')


def hamsu(sy, sx):
    result[sy][sx] = 1  # 방문 처리
    dyx = ((0, 1), (1, 0), (0, -1), (-1, 0))  # 오른쪽, 아래, 왼쪽 순서

    for dy, dx in dyx:
        ny, nx = sy + dy, sx + dx
        # 갈 수 있는 위치인지 판별
        if 0 <= ny <= box_size - 1 and 0 <= nx <= box_size - 1:
            if result[ny][nx] == 0:
                hamsu(ny, nx)
                # 만약에 종료지점에 다다르면
            elif result[ny][nx] == 3:
                return 1

T = int(input())
for tc in range(1,T+1):
    result = []
    box_size = int(input())
    for _ in range(box_size):
        result.append(list(map(int, input())))
    for i in range(box_size):
        if result[4][i] == 2:
            start_x = i
    sy, sx = 0, start_x
    answer = hamsu(sy, sx)
    print(answer)
