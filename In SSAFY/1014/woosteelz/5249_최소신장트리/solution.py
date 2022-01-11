import sys
sys.stdin = open('1014/woosteelz/5249_최소신장트리/sample_input.txt')

for tc in range(int(input())):
    V, E = map(int, input().split())
    graph = [[0 for _ in range(V + 1)] for _ in range(V + 1)]
    visited = [False for _ in range(V + 1)]
    key = [float('inf') for _ in range(V + 1)]
    for _ in range(E):
        a, b, c = map(int, input().split())
        graph[a][b] = c
        graph[b][a] = c

    key[0] = 0

    for i in range(V + 1):
        min_weight = float('inf')
        min_node = -1

        for n in range(V + 1):
            if not visited[n] and key[n] < min_weight:
                min_weight = key[n]
                min_node = n

        visited[min_node] = True

        for n in range(V + 1):
            if graph[min_node][n] and not visited[n] and key[n] > graph[min_node][n]:
                key[n] = graph[min_node][n]

    print(f'#{tc+1} {sum(key)}')
