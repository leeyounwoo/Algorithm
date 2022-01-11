import sys
sys.stdin = open('input.txt')

def dfs(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v, end = ' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in range(1, max(arr) + 1):
        if graph[v][i] == 1 and visited[i] == 0:
            dfs(graph, i, visited)

visited = [False] * 10

arr = list(map(int, input().split()))
graph = [[0] * (max(arr) + 1) for i in range(max(arr) + 1)]
for i in range(0, len(arr), 2):  # 0, 1, 2, 3, 4, 5, 6, 7...
    graph[arr[i]][arr[i+1]] = 1
    graph[arr[i+1]][arr[i]] = 1
dfs(graph, 1, visited)
