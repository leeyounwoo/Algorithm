# 1 2 4 6 5 7 3

def dfs(v):
    # 방문 처리
    # visited 노드 이름이 숫자 1부터 시작이므로 V+1
    visited = [0] * (V + 1)

    print('-{}'.format(v), end='')
    stack = [v]

    while stack:
        visited[v] = 1

        for w in range(1, V+1):
            if adj[v][w] == 1 and visited[w] == 0:
                print('-{}'.format(w), end='')
                stack.append(w)
                v = w
                break
        else:
            if stack:
                v = stack.pop()
            else:
                break

'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

# 정점 수, 간선 수
V, E = map(int, input().split())
# 간선들
edges = list(map(int, input().split()))

# 인접 행렬 초기화
adj = [[0] * (V+1) for _ in range(V+1)]
# 인접 행렬에 간선 표시
for i in range(E):
    s, e = edges[2*i], edges[2*i + 1]
    adj[s][e] = 1
    adj[e][s] = 1

# 인접 행렬 확인
# for i in range(V+1):
#     print('{} | {}'.format(i, adj[i]))

# dfs 탐색하기
dfs(1)