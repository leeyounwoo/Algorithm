import sys
sys.stdin = open('input.txt')

def dfs(v):
    stack = []
    stack.append(v)

    while stack:
        v = stack.pop()

        if visited[v] == 0:
            visited[v] = 1
            print(v)

            for w in range(1, V+1):
                if Graph[v][w] == 1 and visited[w] == 0:
                    stack.append(w)


T = int(input())

for tc in range(1, T+1):
    # input 받기
    V, E = map(int, input().split())
    temp = []
    for _ in range(E):
        temp += list(map(int, input().split()))
    S, G = map(int, input().split())

    Graph = [[0 for _ in range(V + 1)] for _ in range(V + 1)]
    visited = [0 for _ in range(V + 1)]

    for i in range(0, len(temp) - 1, 2):
        Graph[temp[i]][temp[i + 1]] = 1  # 인접한 노드 표기

    print('#{}'.format(tc))
    dfs(S)

    # for i in range(V+1):
    #     for j in range(V+1):
    #         print(Graph[i][j], end=" ")
    #     print()


