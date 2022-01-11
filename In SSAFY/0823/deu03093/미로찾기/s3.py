import sys
sys.stdin = open('input.txt')
# 재귀로 풀기
# 다른건 함수의 인자로 path도 넣어줌
def dfs(si, sj):
    global path
    maze[si][sj] = 1
    dyx = ((0, 1), (1, 0), (0, -1))

    for di, dj in dyx:
        nxi, nxj = si + di, sj + dj
        if 0 <= nxi < N and 0 <= nxj < N:
            if maze[nxi][nxj] == 0:
                if nxi == N-1 and nxj == N-1:
                    path += [(nxi, nxj)]
                    return

                path += [(nxi, nxj)]
                dfs(nxi, nxj)

N = int(input())
maze = [list(map(int, input().split())) for _ in range(N)]
si, sj = 0, 0
# 재귀로 풀 때는
path = []
print(dfs(si, sj))
print(path)