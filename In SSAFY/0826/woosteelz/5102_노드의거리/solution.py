import sys
sys.stdin = open('input.txt')

TC = int(input())
for tc in range(TC):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    visited = [0 for _ in range(V + 1)]
    # 인접 리스트로 초기화
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    start, end = map(int, input().split())

    queue = []
    queue.append(start)
    visited[start] = 1
    while queue:
        curr = queue.pop(0)
        for node in graph[curr]:
            if not visited[node]:
                visited[node] = visited[curr] + 1
                queue.append(node)

    ans = visited[end] - 1 if visited[end] else 0

    print('#{} {}'.format(tc+1, ans))