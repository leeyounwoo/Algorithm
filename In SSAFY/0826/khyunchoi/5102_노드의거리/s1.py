import sys
sys.stdin = open('input.txt')


# def bfs(v):
#     queue = []
#     queue.append(v)
#
#     while queue:
#         new_v = queue.pop(0)
#
#         if not visited[new_v]:
#             visited[new_v] = 1
#
#             for nb in range(1, V+1):
#                 if graph[new_v][nb] == 1 and visited[nb] == 0:
#                     queue.append(nb)
#                     distance[nb] = distance[new_v] + 1
#
#                     if nb == G:
#                         return


def bfs(v):
    queue = []
    queue.append(v)
    visited[v] = 1

    while queue:
        new_v = queue.pop(0)

        for nb in range(1, V+1):
            if graph[new_v][nb] == 1 and visited[nb] == 0:
                queue.append(nb)
                visited[nb] = 1
                distance[nb] = distance[new_v] + 1

                if nb == G:
                    return


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        x, y = map(int, input().split())
        graph[x][y] = 1
        graph[y][x] = 1
    visited = [0 for _ in range(V+1)]
    distance = [0 for _ in range(V+1)]
    S, G = map(int, input().split())

    bfs(S)
    print('#{} {}'.format(tc, distance[G]))