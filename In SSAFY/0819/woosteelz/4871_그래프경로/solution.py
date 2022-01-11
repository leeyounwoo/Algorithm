import sys
sys.stdin = open('input.txt')

def dfs(start, end, visited, graph):
    stack = []
    stack.append(start)
    while stack:
        curr = stack[-1]
        visited[curr] = True
        if curr == end:
            return True
        for next_v in graph[curr]:
            if not visited[next_v]:
                stack.append(next_v)
                break
        else:
            stack.pop()
    return False

TC = int(input())
for tc in range(TC):
    vertex, edge = map(int, input().split())
    # 방문여부
    visited = [False for _ in range(vertex+1)]
    # 방향정보
    graph = [[] for _ in range(vertex+1)]
    for _ in range(edge):
        # 단방향 그래프
        a, b = map(int, input().split())
        graph[a].append(b)

    start, end = map(int, input().split())

    ans = 0
    if dfs(start, end, visited, graph):
        ans = 1
    print('#{} {}'.format(tc+1, ans))