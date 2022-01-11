import sys
sys.stdin = open('input.txt')


def indextocoord(i, j, n):
    # 인덱스를 cartesian 2차원 좌표로 변환하는 함수입니다.
    # i, j는 배열의 인덱스이고, n은 인덱스의 크기입니다.
    # 배열의 가운데가 (0, 0)입니다.
    center = (n-1)/2
    return j - center, -i + center


def rotate90cw(x, y):
    # cartesian 좌표계에서 2차원 회전 행렬은 다음과 같습니다.
    # |cos(θ) -sin(θ)|
    # |sin(θ) cos(θ) |
    # 본 문제에서 돌리는 각도는 θ = -90 (90, 시계방향)입니다.
    # 따라서 다음과 같이 변환합니다.
    return y, -x


def coordtoindex(x, y, n):
    # cartesian 2차원 좌표를 인덱스로 변환하는 함수입니다.
    # i, j는 배열의 인덱스이고, n은 인덱스의 크기입니다.
    # 배열의 가운데가 (0, 0)입니다.
    center = (n-1)/2
    return int(round(-y + center)), int(round(x + center))


T = int(input())

for tc in range(1, T + 1):

    # 배열의 크기를 입력받습니다.
    N = int(input())

    # 2차원 배열을 입력받습니다.
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 90도 돌린 배열을 만들기 위해 초기화합니다.
    mat1 = [[0 for col in range(N)] for row in range(N)]
    # matrix의 모든 원소를 90도 돌립니다.
    for i in range(N):
        for j in range(N):
            # i, j를 x, y로 바꾸고 돌린 뒤 다시 i, j로 변환합니다.
            x, y = indextocoord(i, j, N)
            x, y = rotate90cw(x, y)
            new_i, new_j = coordtoindex(x, y, N)
            mat1[new_i][new_j] = matrix[i][j]

    # 180도 돌린 배열을 만들기 위해 초기화합니다.
    mat2 = [[0 for col in range(N)] for row in range(N)]
    # mat1의 모든 원소를 90도 돌립니다.
    for i in range(N):
        for j in range(N):
            # i, j를 x, y로 바꾸고 돌린 뒤 다시 i, j로 변환합니다.
            x, y = indextocoord(i, j, N)
            x, y = rotate90cw(x, y)
            new_i, new_j = coordtoindex(x, y, N)
            mat2[new_i][new_j] = mat1[i][j]

    # 270도 돌린 배열을 만들기 위해 초기화합니다.
    mat3 = [[0 for col in range(N)] for row in range(N)]
    # mat2의 모든 원소를 90도 돌립니다.
    for i in range(N):
        for j in range(N):
            # i, j를 x, y로 바꾸고 돌린 뒤 다시 i, j로 변환합니다.
            x, y = indextocoord(i, j, N)
            x, y = rotate90cw(x, y)
            new_i, new_j = coordtoindex(x, y, N)
            mat3[new_i][new_j] = mat2[i][j]

    # 결과를 출력합니다.
    print('#{} '.format(tc))
    for i in range(N):
        result = ''.join(map(str, mat1[i])) + ' ' + ''.join(map(str, mat2[i])) + ' ' + ''.join(map(str, mat3[i]))
        print(result)
