import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    arr = []
    result = 0
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    dx = [-1, 0, 1, 0] # 좌 상 우 하
    dy = [0, -1, 0, 1]
    for i in range(N):
        for j in range(N):
            for d in range(4):
                move_y = i + dy[d]
                move_x = j + dx[d]
                if 0<= move_x < N and 0<= move_y < N:
                    result += abs(arr[i][j] - arr[move_y][move_x])

    print("#{} {}".format(tc+1, result))
