import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()


def bfs(start_i, start_j, end_i, end_j):
    visited = [[False] * n for _ in range(n)]
    q = deque([[start_i, start_j, 0]])
    visited[start_i][start_j] = True

    while q:
        now_i, now_j, cnt = q.popleft()
        if now_i == end_i and now_j == end_j:
            return cnt
        for k in range(8):
            next_i, next_j = now_i + di[k], now_j + dj[k]
            if 0 <= next_i < n and 0 <= next_j < n and not visited[next_i][next_j]:
                visited[next_i][next_j] = True
                q.append([next_i, next_j, cnt+1])



di, dj = [-2, -1, 1, 2, 2, 1, -1, -2], [1, 2, 2, 1, -1, -2, -2, -1]
sys.stdin = open('input.txt')
for _ in range(int(input())):
    n = int(input())
    start_i, start_j = map(int, input().split())
    end_i, end_j = map(int, input().split())
    ans = bfs(start_i, start_j, end_i, end_j)
    print(ans)