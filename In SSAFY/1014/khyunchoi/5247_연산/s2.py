import sys
sys.stdin = open('input.txt')

from collections import deque


def calc(N):
    queue = deque()
    queue.append((N, 0))

    while queue:
        num, cnt = queue.popleft()

        if num > 1000000:
            continue

        if visited[num]:
            continue
        visited[num] = 1

        if num == M:
            return cnt

        queue.append((num + 1, cnt + 1))
        queue.append((num - 1, cnt + 1))
        queue.append((num * 2, cnt + 1))
        queue.append((num - 10, cnt + 1))


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [0] * 1000001

    result = calc(N)
    print('#{} {}'.format(tc, result))
