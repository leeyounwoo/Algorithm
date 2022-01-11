import sys
sys.stdin = open('input.txt')


INF = 100000000


def dijkstra_out(N, graph, start):
    D = [INF for _ in range(N)]
    D[start] = 0
    visited = [0 for _ in range(N)]

    for _ in range(N):
        min_path = INF
        min_node = -1
        for i in range(N):
            if not visited[i] and min_path > D[i]:
                min_path = D[i]
                min_node = i

        visited[min_node] = 1

        for i in range(N):
            if graph[min_node][i] and not visited[i]:
                if D[i] > min_path + graph[min_node][i]:
                    D[i] = min_path + graph[min_node][i]

    return D


def dijkstra_in(N, graph, start):
    D = [INF for _ in range(N)]
    D[start] = 0
    visited = [0 for _ in range(N)]

    for _ in range(N):
        min_path = INF
        min_node = -1
        for i in range(N):
            if not visited[i] and min_path > D[i]:
                min_path = D[i]
                min_node = i

        visited[min_node] = 1

        for i in range(N):
            if graph[i][min_node] and not visited[i]:
                if D[i] > min_path + graph[i][min_node]:
                    D[i] = min_path + graph[i][min_node]

    return D


T = int(input())

answer = []
for tc in range(1, T + 1):

    N, M, X = map(int, input().split())
    X = X - 1

    graph = [[0 for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        graph[x - 1][y - 1] = c

    X_to_N = dijkstra_out(N, graph, X)
    N_to_X = dijkstra_in(N, graph, X)

    result = 0
    for i in range(N):
        distance = X_to_N[i] + N_to_X[i]
        if result < distance:
            result = distance

    answer.append(result)

for tc in range(1, T + 1):
    print(f'#{tc} {answer[tc-1]}')