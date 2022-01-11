import sys
sys.stdin = open('input.txt')

def bfs(v):  # v: 출발 노드
    queue = []
    visited = [0] * (V+1)   # V: 노드의 개수
    queue.append(v)

    while queue:
        new_v = queue.pop(0)  # 지금부터 방문할 곳

        if not visited[new_v]:  # 방문한 적이 없다면
            visited[new_v] = 1  # 방문 처리 (== 현재 노드를 방문했다는 뜻)
            print(new_v, end=" ")

            for nb in range(1, 1+V):  # nb: 이웃 노드
                # 현재 노드 (new_v)와 연결되어 있고 (G[new_v][nb] == 1)
                # 다음에 방문할 노드(nb)가 방문한 적이 없다면 (visited[nb] == 0)
                if Graph[new_v][nb] == 1 and visited[nb] == 0:
                    queue.append(nb)


T = int(input())
for tc in range(1, T+1):
    # input 받기
    V, E = map(int, input().split())
    temp = []
    for _ in range(E):
        temp += list(map(int, input().split()))
    S, G = map(int, input().split())
    Graph = [[0 for _ in range(V + 1)] for _ in range(V + 1)]


    for i in range(len(temp), 2):
        Graph[temp[i]][temp[i + 1]] = 1  # 인접한 노드 표기
        Graph[temp[i + 1]][temp[i]] = 1

    bfs(S)
    # print('#{}'.format(tc))

