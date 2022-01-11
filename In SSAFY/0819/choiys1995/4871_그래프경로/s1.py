import sys
sys.stdin = open('input.txt')

T = int(input())

def dfs(start, end):
    stack = []
    stack.append(start) # 스택에 출발 노드 넣기

    while stack:
        v = stack.pop() # 방문 하려는 노드

        if visited[v] == 0:
            visited[v] = 1 # 방문 했습니다.

            for w in range(1, V+1): # 인접 노드 순회
                if G[v][w] == 1 and visited[w] == 0: # 인접 노드중 갈 수 있는 곳이라면
                    stack.append(w)

    if visited[end]: # 방문 노드 목록에 end 노드값이 존재하면
        return 1
    else:
        return 0

for tc in range(1, T+1):
    V, E = map(int, input().split())
    G = [[0 for _ in range(V+1)] for _ in range(V+1)] # 인접 행렬
    visited = [0 for _ in range(V + 1)] # 방문할 배열

    for _ in range(E):
        con1, con2 = map(int, input().split()) # 연결 노드 맵핑
        G[con1][con2] = 1 # 연결된 곳은 1로

    start, end = map(int, input().split()) # 출발노드, 도착 노드 맵핑

    print('#{} {}'.format(tc, dfs(start, end)))