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

            for w in range(1, 100):
                if G[v][w] == 1 and visited[w] == 0:
                    stack.append(w)
                    result.append(w)


for tc in range(1, 11):
    N, V = map(int, input().split())
    temp = list(map(int, input().split()))
    G = [[0 for _ in range(100)] for _ in range(100)]
    visited = [0 for _ in range(100)]
    for i in range(0, len(temp) - 1, 2):
        G[temp[i]][temp[i + 1]] = 1
    dfs(0)
    if 99 in result:
        if 0 in result:
            if result.index(0) > result.index(99):
                    print("#{} 1".format(tc))
            else:
                print("#{} 1".format(tc))
        else:
            print("#{} 0".format(tc))
