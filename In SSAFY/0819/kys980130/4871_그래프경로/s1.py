import sys
sys.stdin = open("input.txt")
result = []
def dfs(v):
    stack = []
    stack.append(v)
    while stack:
        v = stack.pop()
        if visited[v] == 0:
            visited[v] = 1

            for w in range(1, V+1):
                if visited[w] == 0 and G[v][w] == 1:
                    stack.append(w)
                    result.append(w)
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    temp = []
    for i in range(E):
        a, b = map(int, input().split())
        temp.append(a)
        temp.append(b)
    start, end = map(int, input().split())

    G = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]
    for i in range(0, len(temp)-1, 2):
        G[temp[i]][temp[i+1]] = 1
    dfs(start)
    if end in result:
        print("#{} 1".format(tc))
    else:
        print("#{} 0".format(tc))