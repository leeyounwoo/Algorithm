import sys
sys.stdin = open('input.txt')

def path_finder(arr):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                x, y = i, j # 출발점 찾기
                # print(x, y, '#$$')
    # 좌 상 우 하
    dxy = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        arr[x][y] = 1

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if 0 <= nx <= n-1 and 0 <= ny <= n-1:
                if arr[nx][ny] == 3:
                    return 1

                if arr[nx][ny] == 0:
                    stack.append((nx, ny))
                    # print(nx, ny, '####')
    return 0



t = int(input())

for tc in range(1, t+1):
   n = int(input())
   arr = [list(map(int, input())) for _ in range(n)]
   result = path_finder(arr)
   print('#{} {}'.format(tc, result))