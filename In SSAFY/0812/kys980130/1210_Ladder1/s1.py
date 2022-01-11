import sys
sys.stdin = open("input.txt")
dy = [0, 1, 0, -1]  # 상우하좌
dx = [-1, 0, 1, 0]
for tc in range(10):
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    for i in range(100):
        for j in range(100):
            if ladder[i][j] == 2:
                x, y = i, j
    if x == 1 or y == 1:
        dir = (dir+1) % 4
        x = x + dx[dir]
        y = y + dy[dir]
    print(x, y)