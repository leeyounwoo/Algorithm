import sys
sys.stdin = open('input.txt')


def DFS(nodemap, visited, v):
    if v == -1:
        result = 0
        for vertex in range(len(nodemap)):
            new_visited = visited[:]
            new_visited[vertex] = 1
            temp = DFS(nodemap, new_visited, vertex)
            if result < temp:
                result = temp
        return result
    else:
        w = []
        for i in range(len(nodemap[v])):
            if nodemap[v][i] == 1 and not visited[i]:
                w.append(i)

        if not w:
            return 1
        else:
            tempmax = 0
            for i in w:
                new_visited = visited[:]
                new_visited[i] = 1
                temp = DFS(nodemap, new_visited, i)
                if tempmax < temp:
                    tempmax = temp
            return tempmax + 1


T = int(input())

answer = []
for tc in range(1, T + 1):

    N, M = map(int, input().split())

    nodes = []
    for _ in range(M):
        a, b = map(int, input().split())
        nodes.append([a - 1, b - 1])

    nodemap = [[0 for _ in range(N)] for _ in range(N)]
    for node in nodes:
        a, b = node
        nodemap[a][b] = 1
        nodemap[b][a] = 1

    visited = [0] * N

    result = 0
    if M == 0:
        result = 1
    elif M == 1:
        result = 2
    else:
        result = DFS(nodemap, visited, -1)

    answer.append(result)

for tc in range(1, T + 1):
    print(f'#{tc} {answer[tc-1]}')