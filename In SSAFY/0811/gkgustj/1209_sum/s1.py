import sys

sys.stdin = open('input.txt')

for _ in range(1, 11):
    # 테스트 케이스 번호
    t = int(input())
    
    # 배열 입력 받기
    arr = []
    for _ in range(100):
        row = list(map(int, input().split()))
        arr.append(row)

    max_row = 0
    max_col = 0
    max_diag = 0
    sum_diag = 0

    for i in range(len(arr)):
        # 행의 합 중 최대 구하기
        if sum(arr[i]) > max_row:
            max_row = sum(arr[i])
        for j in range(len(arr[i])):
            # 2개의 대각선 합 구하기
            if i == j:
                sum_diag += arr[i][j]
            elif i+j == len(arr)-1:
                max_diag += arr[i][j]
    
    # 대각선 2개 합 비교해서 최대값 저장
    if sum_diag > max_diag:
        max_diag = sum_diag

    # 열의 합 중 최대 구하기
    for j in range(len(arr[0])):
        sum_col = 0
        for i in range(len(arr)):
            sum_col += arr[i][j]
        if sum_col > max_col:
            max_col = sum_col
    
    # 행의 합, 열의 합, 대각선 합 중 최대값 저장
    result = max_row
    if max_col > result:
        result = max_col
    if max_diag > result:
        result = max_diag

    print(f'#{t} {result}')