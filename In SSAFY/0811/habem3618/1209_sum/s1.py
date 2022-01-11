import sys
sys.stdin = open('input.txt')

for tc in range(10):
    number = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    result = []

    # 행과 열의 합
    for i in range(len(arr)):
        total_x = 0
        total_y = 0
        for j in range(len(arr[i])):
            total_x += arr[i][j]
            total_y += arr[j][i]
    # 결과값에 행과 열의 합 추가
            result.append(total_x)
            result.append(total_y)

    # 양 대각선의 합
    total_z1 = 0
    total_z2 = 0
    for i in range(len(arr)):
        total_z1 += arr[i][i]
        total_z2 += arr[99-i][i]
    # 결과값에 양 대각선의 합 추가
        result.append(total_z1)
        result.append(total_z2)

    # 결과값에서 최댓값 구하기
    max_val = result[0]
    for i in range(1, len(result)):
        if max_val < result[i]:
            max_val = result[i]

    print('#{} {}'.format(tc + 1, max_val))
