import sys
from collections import deque

sys.stdin = open('1005/woosteelz/1861_정사각형방/input.txt')
dir_x = [0, 1, -1, 0]
dir_y = [1, 0, 0, -1]


def bfs(x, y):
    global N

    cnt = 0

    queue = deque()
    queue.append([x, y])
    while queue:
        curr_x, curr_y = queue.popleft()
        for i in range(4):
            next_x, next_y = curr_x + dir_x[i], curr_y + dir_y[i]
            if 0 <= next_x < N and 0 <= next_y < N and graph[next_x][next_y] == graph[curr_x][curr_y] + 1:
                cnt += 1
                queue.append([next_x, next_y])

    return cnt


for tc in range(int(input())):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    ans = []

    for i in range(N):
        for j in range(N):
            ans.append([graph[i][j], bfs(i, j)])

    ans.sort(key=lambda x: (-x[1], x[0]))
    print(f'#{tc+1} {ans[0][0]} {ans[0][1]}')
