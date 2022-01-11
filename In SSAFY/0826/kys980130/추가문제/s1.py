import sys
sys.stdin = open("input.txt")
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    map_info = [list(input()) for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if map_info[i][j] == 'A':
                for m in range(-1, 2):
                    if map_info[i+m][j] == 'H':
                        map_info[i+m][j] = 'X'
                    if map_info[i][j+m] == 'H':
                        map_info[i][j+m] = 'X'
            elif map_info[i][j] == 'B':
                for m in range(-2, 3):
                    if map_info[i + m][j] == 'H':
                        map_info[i+m][j] = 'X'
                    if map_info[i][j + m] == 'H':
                        map_info[i][j+m] = 'X'
            elif map_info[i][j] == 'C':
                for m in range(-3, 4):
                    if map_info[i + m][j] == 'H':
                        map_info[i+m][j] = 'X'
                    if map_info[i][j + m] == 'H':
                        map_info[i][j+m] = 'X'
    for x in range(N):
        for y in range(N):
            if map_info[x][y] == 'H':
                count += 1
    print('#{} {}'.format(tc, count))

