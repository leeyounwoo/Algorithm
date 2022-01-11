import sys
sys.stdin = open('input.txt')

for tc in range(10):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_num = 0

    for i in range(100):
        sum_num_row = 0
        sum_num_col = 0
        for j in range(100):
            sum_num_row += arr[i][j]
            sum_num_col += arr[j][i]
        if sum_num_row > max_num:
            max_num = sum_num_row
        if sum_num_col > max_num:
            max_num = sum_num_col

    for i in range(100):
        sum_right_cross = 0
        sum_right_cross += arr[i][i]
    if sum_right_cross > max_num:
        max_num = sum_right_cross

    for i in range(99, -1, -1):
        sum_left_cross = 0
        sum_left_cross += arr[i][i]
    if sum_left_cross > max_num:
        max_num = sum_left_cross

    print("#{} {}".format(tc+1, max_num))

