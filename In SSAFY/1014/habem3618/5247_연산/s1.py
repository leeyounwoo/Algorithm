import sys
sys.stdin = open('input.txt')
from collections import deque


def bfs():
    global result

    while queue:

        n, cnt = queue.popleft()

        if n == M:
            result = cnt
            return

        temp = n + 1
        if 0 < temp <= 1000000 and not visited[temp]:
            queue.append((temp, cnt + 1))
            visited[temp] = True

        temp = n - 1
        if 0 < temp <= 1000000 and not visited[temp]:
            queue.append((temp, cnt + 1))
            visited[temp] = True

        temp = n * 2
        if 0 < temp <= 1000000 and not visited[temp]:
            queue.append((temp, cnt + 1))
            visited[temp] = True

        temp = n - 10
        if 0 < temp <= 1000000 and not visited[temp]:
            queue.append((temp, cnt + 1))
            visited[temp] = True


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    visited = [False] * 1000001
    result = 0
    queue = deque()
    queue.append((N, 0))
    bfs()

    print("#{} {}".format(tc, result))
