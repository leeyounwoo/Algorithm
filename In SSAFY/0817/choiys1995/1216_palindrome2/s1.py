import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    input()
    arr = [list(input()) for _ in range(100)]
    # 세로부터 읽은 2차원 배열
    arr2 = [[arr[i][j] for i in range(100)] for j in range(100)]

    cnt = 100
    flag = 0
    while cnt > 0:
        # 연산해야할 자리는 몇개?
        for row in range(100 - cnt + 1):
            for col in range(100 - cnt + 1):
                if arr[row][col : col + cnt] == arr[row][col : col + cnt][ : :-1]:
                    flag = 1
                if arr[row][col : col + cnt] == arr[row][col : col + cnt][ : :-1]:
                    flag = 1
        if flag == 1:
            break
        cnt -= 1
    print('#{} {}'.format(tc, cnt))
