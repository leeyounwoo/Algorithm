import sys
sys.stdin = open('input.txt')

for tc in range(10):
    n = input()
    ladder = [list(map(int, input().split())) for _ in range(100)]
    visited = [[False for _ in range(100)] for _ in range(100)]

    dir_x = [0, 0]
    dir_y = [1, -1]
    # 도착위치 탐색
    curr_x, curr_y = 99, 99
    for i in range(100):
        if ladder[99][i] == 2:
            curr_y = i
            break

    visited[curr_x][curr_y] = True
    while True:
        if curr_x == 0:
            break
        next_x, next_y = curr_x - 1, curr_y
        for i in range(2):
            temp_x, temp_y = curr_x + dir_x[i], curr_y + dir_y[i]
            if 0 <= temp_x < 100 and 0 <= temp_y < 100 and ladder[temp_x][temp_y] and not visited[temp_x][temp_y]:
                next_x = temp_x
                next_y = temp_y

        visited[next_x][next_y] = True
        curr_x = next_x
        curr_y = next_y
    print('#{} {}'.format(tc+1, curr_y))

