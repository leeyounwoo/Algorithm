import sys
sys.stdin = open('input.txt')

def check_row(arr):
    for i in range(9):
        check = [0] * 9

        for j in range(9):
            # arr안에는 1~9 -> check의 인덱스 0~8
            check[arr[i][j] - 1] += 1

        if 0 in check:
            return
    return check


def check_col(arr):
    for j in range(9):
        check = [0] * 9

        for i in range(9):
            check[arr[i][j] - 1] += 1

        if 0 in check:
            return
    return check


def check_box(arr):
    for i in (0, 3, 6):
        for j in (0, 3, 6):
            check = [0] * 9
            for k in range(i, i+3):
                for l in range(j, j+3):
                    check[arr[k][l] - 1] += 1
            if 0 in check:
                return
    return check


T = int(input())

for t in range(1, T+1):
    arr = []

    for _ in range(9):
        arr.append(list(map(int, input().split())))

    result = 0

    if check_row(arr):
        if check_col(arr):
            if check_box(arr):
                result = 1

    print('#{} {}'.format(t, result))