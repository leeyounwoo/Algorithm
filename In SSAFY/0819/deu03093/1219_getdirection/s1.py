import sys

sys.stdin = open('input.txt')
def dfs(start, end):
    stack = []
    check = [False] * 100
    check[start] = True
    for i in edges[start]:
        stack.append(i)
    while stack:
        now = stack.pop()
        check[now] = True
        for i in edges[now]:
            if not check[i]:
                if i == end:
                    return 1
                stack.append(i)
    return 0


for T in range(1, 11):
    tc, E = map(int, input().split())
    check = [False] * 100
    edges = [[] for _ in range(100)]
    edge_string = list(map(int, input().split()))
    for i in range(len(edge_string)//2):
        edges[edge_string[i*2]].append(edge_string[i*2+1])
    ans = dfs(0, 99)
    print('#{} {}'.format(T, ans))