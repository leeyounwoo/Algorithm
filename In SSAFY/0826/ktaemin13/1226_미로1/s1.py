import sys
sys.stdin = open('input.txt')


def maze():

    ans = 0

    dir_x = [0, -1, 0, 1]
    dir_y = [1, 0, -1, 0]
    stack = []
    # 시작위치 탐색
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                stack.append([i, j])

    while stack:
        curr_x, curr_y = stack.pop()

        if arr[curr_x][curr_y] == 3:
            ans = 1

        arr[curr_x][curr_y] = 1

        for i in range(4):
            next_x, next_y = curr_x + dir_x[i], curr_y + dir_y[i]
            if 0 <= next_x < 16 and 0 <= next_y < 16 and not arr[next_x][next_y] == 1:
                stack.append([next_x, next_y])
    return ans



for tc in range(10):
    N = input()
    arr = [list(map(int, (input()))) for _ in range(16)]
    print('#{} {}'.format(tc+1, maze()))