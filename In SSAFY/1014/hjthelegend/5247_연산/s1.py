import sys
sys.stdin = open('input.txt')
from collections import deque

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    # n -> m 최소 횟수
    # +1, -1, *2, -10
    queue = deque([(n, 0)])
    visited = set()
    visited.add(n)
    while queue:
        n, count = queue.popleft()
        if n == m:
            break

        # 1<=N, M<=1,000,000, N!=M
        if n+1 not in visited and n+1 <= 1000000:
            queue.append((n+1, count+1))
            visited.add(n+1)
        if n-1 not in visited and n-1 <= 1000000:
            queue.append((n-1, count+1))
            visited.add(n-1)
        if n*2 not in visited and n*2 <= 1000000:
            queue.append((n*2, count+1))
            visited.add(n*2)
        if n-10 not in visited and n-10 <= 1000000:
            queue.append((n-10, count+1))
            visited.add(n-10)

    print('#{} {}'.format(tc, count))