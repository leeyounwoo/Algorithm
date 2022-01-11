import sys
sys.stdin = open('input.txt')

def dfs(v): # v: 시작정점
    # visited 체크
    visited[v] = True
    # 방문하지 않았으면
    for w in range(1, V+1):
        if adj[v][w] == 1 and visited[w] == 0:
            # 다시 dfs(w) 재귀 호출
            dfs(w)
T = 10

for tc in range(1, T+1):

    V = 100
    N, E = map(int, input().split())
    tmp = list(map(int, input().split()))
    adj = [[0] * (V+1) for _ in range(V+1)] # 인접행렬 초기화
    visited = [0] * (V+1)

    # 입력
    for i in range(E):
        s, e = tmp[2*i], tmp[2*i+1]
        adj[s][e] = 1

    print("#{}".format(tc), end=' ')
    dfs(0)
    if visited[99] == True:
        print(1)
    else:
        print(0)