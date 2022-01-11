import sys
sys.stdin = open('input.txt')
# 재귀
def dfs(sy, sx, path):
    maze[sy][sx] = 1 # 방문 처리
    dyx = ((0, 1), (1, 0), (0, -1))  # 오른쪽, 아래, 왼쪽

    for dy, dx in dyx:
        ny, nx = sy + dy, sx + dx
        # 갈 수 있는 위치인지 판별
        if 0 <= ny <= N-1 and 0 <= nx <= N-1:
            if maze[ny][nx] == 0:
                # 만약에 종료지점에 다다르면
                if ny == N-1 and nx == N-1:
                    print(path)
                    return
                dfs(ny, nx, path + [[ny, nx]])



N = int(input())
maze = [list(map(int, input().split())) for _ in range(N)]

sy, sx = 0, 0
result = dfs(sy, sx, [])
print(result)