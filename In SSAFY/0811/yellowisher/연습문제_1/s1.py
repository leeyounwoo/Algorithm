import sys
sys.stdin = open('input.txt')

T = int(input())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(5)]
    sum_num = 0
    for x in range(5):
        for y in range(5):
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if (-1 < nx < 5) and (-1 < ny < 5):
                    sum_num += abs(arr[nx][ny] - arr[x][y])
    print("#{} {}".format(tc+1, sum_num))