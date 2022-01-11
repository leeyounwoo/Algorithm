T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    
    # 맨 위쪽 & 왼쪽 테두리 처리
    for i in range(1, N):
        mat[0][i] += mat[0][i-1]
        mat[i][0] += mat[i-1][0]

    for y in range(1, N):
        for x in range(1, N):
            mat[y][x] += min(mat[y-1][x], mat[y][x-1])

    print(f'#{tc} {mat[N-1][N-1]}')