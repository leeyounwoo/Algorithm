import sys
sys.stdin = open('input.txt')

# T는 테스트 케이스 번호
T = 10

for tc in range(1, T+1):
    N = input()
    arr = []

    # 반복문을 통해 100 * 100 리스트 만들기
    for i in range(100):
        lst = arr.append(list(map(int, input().split())))

    # 가로 합
    max_row = 0
    for i in range(100):
        sum_row = 0
        for j in range(100):
            sum_row += arr[i][j]
        if sum_row > max_row:
            max_row = sum_row

    # 세로 합
    max_col = 0
    for i in range(100):
        sum_col = 0
        for j in range(100):
            sum_col += arr[j][i]
        if sum_col > max_col:
            max_col = sum_col

    # 대각선 합
    max_dia = 0
    for i in range(100):
        sum_right = 0
        sum_left = 0
        sum_right = arr[i][i]
        sum_left = arr[i][99-i]
    if max(sum_right, sum_left) > max_dia:
        max_dia = max(sum_right, sum_left)

    print('#{} {}'.format(tc, max(max_row, max_col, max_dia)))