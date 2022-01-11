import sys
sys.stdin = open('input.txt')

def dfs(x, y):
    stack = [(x, y, [])]
    dxy = ((0, 1), (1, 0), (0, -1)) # 오른쪽 아래 왼쪽

    while stack:
        x, y, path = stack.pop()
        arr[x][y] = 1

        for dx, dy in dxy:
            # 다음 위치
            nx, ny = x + dx, y + dy

            # 갈 수 있는지 판단
            if nx in range(N) and ny in range(N) and arr[nx][ny] == 0:
                if nx == N-1 and ny == N-1:
                    return path

                stack.append((nx, ny, path + [(x, y)]))
                print(stack)


N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

print(dfs(0, 0))