import sys
sys.stdin = open('input.txt')
def dfs(si, sj):
    # 핵심 아이디어
    # 다음 지점으로 갈 때 '필요한 정보를 같이 가져가기'
    stack = [(si, sj, [])]

    dyx = ((0, 1), (1, 0), (0, -1))
    while stack:
        ni, nj, path = stack.pop()
        maze[ni][nj] = 1
        for di, dj in dyx:
            nxi, nxj = ni + di, nj + dj
            # 갈 수 있는지 판단
            # 1. 새로운 위치 (nxi, nxj)가 배열의 범위를 벗어나지 않는지?
            # 2. 새로운 위치 (nxi, nxj)가 벽이 아닌지?
            if 0 <= nxi < N and 0 <= nxj < N:
                if maze[nxi][nxj] == 0:
                    # 종료지점에 도착하면 경로 반환
                    if nxi == N-1 and nxj == N-1:
                        return path + [(ni, nj), (nxi, nxj)]
                    stack.append((nxi, nxj, path + [(ni, nj)]))


N = int(input())
maze = [list(map(int, input().split())) for _ in range(N)]
si, sj = 0, 0
print(dfs(0,0))