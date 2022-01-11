import sys

def dfs(start, end):
    stack = []
    check[start] = True
    for e in edges[start]:
        if not check[e]:
            stack.append(e)
    while stack:
        new_start = stack.pop()
        if new_start == end:
            return 1
        else:
            check[new_start] = True
            for e in edges[new_start]:
                if not check[e]:
                    stack.append(e)
    return 0

sys.stdin = open('input.txt')
for T in range(1, 1+int(input())):
    v, e = map(int, input().split())
    check = [False] * (v + 1)
    edges = [[] for _ in range(v + 1)]
    for _ in range(e):
        s, e = map(int, input().split())
        edges[s].append(e)
    start, end = map(int, input().split())
    ans = dfs(start, end)
    print('#{} {}'.format(T, ans))