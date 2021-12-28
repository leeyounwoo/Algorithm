import sys
sys.stdin = open('input.txt')
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
# 위, 아래, 오른쪽, 왼쪽
def bfs(now_i, now_j):
    global farm_width, farm_height
    for t in range(4):
        next_i, next_j = now_i + dy[t], now_j + dx[t]
        if 0 <= next_i < farm_height and 0 <= next_j < farm_width and check[next_i][next_j]:
            check[next_i][next_j] = False
            bfs(next_i, next_j)
    return

for T in range(int(input())):
    farm_width, farm_height, cnt = map(int, input().split())
    check = [[False] * farm_width for _ in range(farm_height)]
    for _ in range(cnt):
        x, y = map(int, input().split())
        check[y][x] = True
    ans = 0
    for i in range(farm_height):
        for j in range(farm_width):
            if check[i][j]:
                ans += 1
                check[i][j] = False
                bfs(i, j)
    print(ans)