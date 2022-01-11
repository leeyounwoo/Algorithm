'''
5
1 1 1 1 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 1 1 1 1
정답 : 24
'''


# 상 하 좌 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# 2차원 배열 입력 받기

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
total = 0

def my_abs(x):
    if x < 0:
        return -x
    else:
        return x


for i in range(N):
    for j in range(N):
        for k in range(4):
            # 4 방향의 좌표
            next_i = i + di[k]
            next_j = j + dj[k]
            # 벽 체크
            if 0 <= next_i < N and 0 <= next_j < N:
                total += my_abs(arr[i][j] - arr[next_i][next_j])


print(total)