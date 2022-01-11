import sys
sys.stdin = open('input.txt')

from collections import deque


def bfs(start, end):
    stack = deque([start])
    while stack:
        nx = stack.popleft()
        if visited[nx] == 0:
            visited[nx] += 1
        for nb in range(1, V+1):
            if adj[nx][nb] == 1 and visited[nb] == 0:
                stack.append(nb)
                visited[nb] = visited[nx] + 1
        if nx == end:
            return visited[end] - 1
    return 0



T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    node = [list(map(int, input().split())) for _ in range(E)]
    start, end = map(int, input().split())
    visited = [0] * (V + 1)

    adj = [[0]*(V+1) for _ in range(V+1)]
    for nod in node:
        adj[nod[0]][nod[1]] = 1
        adj[nod[1]][nod[0]] = 1

    print('#{} {}'.format(tc+1, bfs(start, end)))
    # print(visited)
    # print(visited[end])



    # adj = {key: [] for key in range(1, V+1)}
    # for key, nod in node:
    #     adj[key].append(nod)
    #
    # stack = [start]
    # visited = []
    # result = 0
    # cnt = -1
    # while stack:
    #     nx = stack.pop(0)
    #     cnt += 1
    #     if len(adj[nx]) == cnt:
    #         result += 1
    #         cnt = 0
    #
    #     # if nx == end:
    #     #     result.append(cnt)
    #     #     break
    #     if nx not in visited:
    #         visited.append(nx)
    #         for ad in adj[nx]:
    #             stack.append(ad)
    #
    # print(result)

