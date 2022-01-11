from collections import deque
import sys
sys.stdin = open('input.txt')

def bfs(i, j, cnt):
    queue = deque()
    queue.append((i, j))

    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        x, y = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x+dx, y+dy

            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == arr[x][y] + 1:
                cnt += 1
                queue.append((nx, ny))
    
    return cnt

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0
    max_num = 0
    for i in range(N):
        for j in range(N):
            cnt = bfs(i, j, 1)
            if cnt > max_cnt:
                max_cnt = cnt
                max_num = arr[i][j]
            elif cnt == max_cnt:
                max_num = min(max_num, arr[i][j])

    print('#{} {} {}'.format(t, max_num, max_cnt))