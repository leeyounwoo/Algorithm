import sys
sys.stdin = open('input.txt')

INF = 100000000


def dijkstra(V, graph):
    D = [INF for _ in range(V)]
    visited = [0 for _ in range(V)]

    # start position: 0
    D[0] = 0

    for _ in range(V):
        v, min_path = -1, INF
        for i in range(V):
            if not visited[i] and min_path > D[i]:
                min_path = D[i]
                v = i

        visited[v] = 1
        for w in range(V):
            if D[v] + graph[v][w] < D[w]:
                D[w] = D[v] + graph[v][w]

    # end position: V-1
    return D[V - 1]


T = int(input())

answer = []
for tc in range(1, T + 1):

    V, E = map(int, input().split())
    V += 1

    graph = [[INF for _ in range(V)] for _ in range(V)]
    for _ in range(E):
        v, w, weight = map(int, input().split())
        graph[v][w] = weight

    result = dijkstra(V, graph)

    answer.append(result)

for tc in range(1, T + 1):
    print(f'#{tc} {answer[tc-1]}')
