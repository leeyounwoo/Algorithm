import sys


def input():
    return sys.stdin.readline().rstrip()


def bfs(start, cnt):
    global ans
    if cnt > ans:
        return
    if start == 100 and ans > cnt:
        ans = cnt
        return
    candidate = []
    for num in range(6, 0, -1):
        candidate.append(start + num)
    if start <= 93:
        flag = False
        for next in candidate:
            if next in up_keys:
                bfs(hash_up[next], cnt+1)
            elif next in down_keys:
                bfs(hash_down[next], cnt + 1)
            elif not flag:
                bfs(next, cnt+1)
                flag = True
    else:
        bfs(100, cnt+1)



sys.stdin = open('input.txt')
n, m = map(int, input().split())
hash_up = {}
hash_down = {}
for _ in range(n):
    start, end = map(int, input().split())
    hash_up[start] = end

for _ in range(m):
    start, end = map(int, input().split())
    hash_down[start] = end

up_keys = list(hash_up.keys())
down_keys = list(hash_down.keys())

ans = 101
bfs(1, 0)
print(ans)
