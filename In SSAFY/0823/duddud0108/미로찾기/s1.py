import sys
sys.stdin = open('input.txt')

def dfs(N, g):
    stack = [(0, 0)]
    visited = []
    dx = [0, 0, 1]
    dy = [1, -1, 0]

    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)

            if v == (N-1, N-1):  # 끝점에 도착하면 방문 기록 return
                return visited

            for i in range(3):
                x, y = v[0]+dx[i], v[1]+dy[i]
                if -1 < x < N and -1 < y < N and g[x][y] == 0:  # 벽이 아니고 0이면 넣어줌
                    stack.append((x, y))
            print(stack)

N = int(input())
g = [list(map(int, input().split())) for _ in range(N)]
print(dfs(N, g))