import sys
sys.stdin = open('input.txt')

for tc in range(10):
    n = input()
    arr_2D = [list(map(int, input().split())) for _ in range(100)]
    # ans = float('-inf')
    ans = -100000001

    # 행 / 열
    for i in range(100):
        temp1 = 0
        temp2 = 0
        for j in range(100):
            temp1 += arr_2D[i][j]
            temp2 += arr_2D[j][i]
        if ans < temp1:
            ans = temp1
        if ans < temp2:
            ans = temp2

    # 대각
    temp1, temp2 = 0, 0
    for i in range(100):
        temp1 += arr_2D[i][i]
        temp2 += arr_2D[99-i][i]

    if ans < temp1:
        ans = temp1
    if ans < temp2:
        ans = temp2

    print('#{} {}'.format(tc+1, ans))