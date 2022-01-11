import sys
sys.stdin = open("input.txt")
T = int(input())

def is_wall(x, y):
    if (new_x > N - 1 or new_x < 0 or new_y > N-1 or new_y < 0 or
                arr[new_y][new_x] != 0):
        return True
    return False


for tc in range(1, T+1):
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)]

    new_x, new_y = 0, 0
    x, y = 0, 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    dir_stat = 0

    for i in range(1, N * N + 1):
        x, y = new_x, new_y
        arr[y][x] = i
        new_x = x + dx[dir_stat]
        new_y = y + dy[dir_stat]

        if is_wall(new_x, new_y): # 벽 검사
            dir_stat = (dir_stat + 1) % 4
            new_x = x + dx[dir_stat]
            new_y = y + dy[dir_stat]

    print('#{}'.format(tc))
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j])


