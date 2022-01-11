import sys
sys.stdin = open('input.txt')

# 재귀로 구현
def dfs(x, y, path):
    arr[x][y] = 1

    dxy = ((0, 1), (1, 0), (0, -1)) # 오른쪽 아래 왼쪽

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy

        if nx in range(N) and ny in range(N) and arr[nx][ny] == 0:
            if nx == N-1 and ny == N-1:
                print(path)
                return

            dfs(nx, ny, path + [(nx, ny)])


N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

print(dfs(0, 0, []))