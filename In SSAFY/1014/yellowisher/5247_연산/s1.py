import sys
sys.stdin=open('input.txt')
from collections import deque

def bfs(N, M):
    queue = deque()
    queue.append((N, 0))

    while queue:
        value, count = queue.popleft()

        if visited[value]: # 비어있지 않으면 건너 뜀
            continue

        visited[value] = 1 # 방문 처리

        if value == M: # 종료 조건
            return count

        if 0 < value + 1 <= 1000000:
            queue.append((value + 1, count + 1))
        if 0 < value - 1 <= 1000000:
            queue.append((value - 1, count + 1))
        if 0 < value * 2 <= 1000000:
            queue.append((value * 2, count + 1))
        if 0 < value - 10 <= 1000000:
            queue.append((value - 10, count + 1))


for t in range(int(input())):
    N, M = map(int, input().split())
    visited = [0] * 1000001
    print('#{} {}'.format(t + 1, bfs(N, M)))