import sys

sys.stdin = open('input.txt')

def find_max(temp): # 최대값 찾는 함수

    tempmax = -1
    for i in temp:
        if tempmax < i:
            tempmax = i

    return tempmax

def find_sum(temp): # 리스트 합 구하는 함수

    tempsum = 0
    for i in temp:
        tempsum += i
    return tempsum

for T in range(1, 11):
    int(input())
    arr = []
    for _ in range(100):
        arr.append(list(map(int, input().split())))
    max_row = max_col = left_diag = right_diag = 0
    ans = 0

    for i in range(100):
        # row의 max를 찾아줌
        if max_row < sum(arr[i]):
            max_row = sum(arr[i])

        # col의 max를 찾아줌
        sum_col = 0
        for j in range(100):
            sum_col += arr[j][i]
        if max_col < sum_col:
            max_col = sum_col

        #양쪽 대각선의 합을 구함
        left_diag += arr[i][i]
        right_diag += arr[i][99-i]

    result = find_max([max_row, max_col, left_diag, right_diag])
    print('#{} {}'.format(T, result))
