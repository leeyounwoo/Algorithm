import sys
sys.stdin = open('input.txt')

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

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

# 순회하기
    total = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):  # 상하좌우 이므로 4번
                # 4방향의 좌표
                ni = i + di[k]
                nj = j + dj[k]
                # 벽체크 : 밖으로 빠져버리므로 설정
                if 0 <= ni < N and 0 <= nj < N:
                    total += my_abs(arr[i][j] - arr[ni][nj])

    print('#{} {}'.format(tc, total))