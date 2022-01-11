from collections import deque
import sys
sys.stdin = open('input.txt')
def bfs(N, M):
    queue = deque()
    queue.append((N, 0))
    while queue:
        v, count = queue.popleft()
        if v == M:
            return count
        if 0 < v+1 <= 1000000 and visited[v+1] == 0:
            queue.append((v+1, count+1))
            visited[v+1] = 1
        if 0 < v-1 <= 1000000 and visited[v-1] == 0:
            queue.append((v-1, count+1))
            visited[v-1] = 1
        if 0 < v*2 <= 1000000 and visited[v*2] == 0:
            queue.append((v*2, count+1))
            visited[v*2] = 1
        if 0 < v-10 <= 1000000 and visited[v-10] == 0:
            queue.append((v-10, count+1))
            visited[v-10] = 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [0] * 1000001
    print('#{} {}'.format(tc, bfs(N, M)))

