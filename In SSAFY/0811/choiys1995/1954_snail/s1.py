import sys
sys.stdin = open('input.txt')

T = int(input())

# row, col 인덱스로 방향 설정 (우->하->좌->상)
delta_row = [0, 1, 0, -1]
delta_col = [1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())
    #2차원 배열
    snail = [[0]*N for _ in range(N)]
    # 초기 위치 & 회전방향 설정
    row, col = 0, 0
    direc = 0  # 방향(0:우, 1:하, 2:좌, 3:상)
    for n in range(1, N**2 + 1):
        snail[row][col] = n
        row += delta_row[direc]
        col += delta_col[direc]

        # 다음 경로가 범위를 벗어난다면 or 0이 아닌 수가 들어와 있다면 방향 변경
        if row < 0 or col < 0 or row >= N or col >= N \
                or snail[row][col] != 0:

            #요소 인덱스 한 칸 전으로
            row -= delta_row[direc]
            col -= delta_col[direc]

            # direc % 4 방향 변경 후 다시 출발
            direc = (direc + 1) % 4
            row += delta_row[direc]
            col += delta_col[direc]

    print('#{}'.format(tc))
    for num in snail:
        print(*num)