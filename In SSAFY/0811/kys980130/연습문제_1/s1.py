import sys
sys.stdin = open("input.txt")

def my_abs(x):
    if x < 0:
        return -x
    else:
        return x

# 상하좌우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# 2차원 배열 입력
T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(4):
                # 4 방향의 좌표
                ni= i + di[k]
                nj = j + dj[k]
                # 벽 체크
                if 0 <= ni < N and 0 <= nj < N:
                    total += my_abs(arr[i][j] - arr[ni][nj])
