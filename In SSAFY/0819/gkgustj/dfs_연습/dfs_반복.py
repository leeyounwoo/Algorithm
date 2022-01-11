'''
7 8   : 노드 수, 간선 수
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7   : 간선간의 연결
'''

import sys
sys.stdin = open(('input.txt'))

def dfs(v):
    stack = []
    stack.append(v)

    while stack:
        v = stack.pop() # 현재 방문하려는 노드

        if visited[v] == 0:
            visited[v] = 1     # 방문 표기
            print(v, end=' ')  # 현재 방문한 노드 출력

            for w in range(1, V+1):  # 인접 노드 순회
                if G[v][w] == 1 and visited[w] == 0:
                    stack.append(w)

V, E = map(int, input().split())
temp = list(map(int, input().split()))

G = [[0 for _ in range(V+1)] for _ in range(V+1)]
visited = [0 for _ in range(V+1)]

for i in range(0, len(temp)-1, 2):
    G[temp[i]][temp[i+1]] = 1
    G[temp[i+1]][temp[i]] = 1

# 인접 행렬 확인
# for i in range(V+1):
#     print('{} | {}'.format(i, adj[i]))

dfs(1)