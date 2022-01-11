import sys
sys.stdin = open('input.txt')

def pascal_triangle(N):

    arr = [[0] * N for _ in range(N)]
    # 양 끝에는 값을 1, 가운데에 있는 값은 바로 위의 값과 바로 위의 값의 왼쪽 값을 더한다.
    for i in range(N):
        for j in range(i + 1):
            if j == 0 or j == i:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i - 1][j] + arr[i - 1][j - 1]

    for r in range(N):
        for c in range(N):
            if arr[r][c] != 0:
                print(arr[r][c], end=' ')
        print()



T = int(input())

for tc in range(T):
    N = int(input())  # 파스칼 삼각형 줄 수

    print('#{}'.format(tc+1))
    pascal_triangle(N)

