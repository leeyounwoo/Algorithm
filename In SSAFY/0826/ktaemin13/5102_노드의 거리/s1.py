import sys
sys.stdin = open('input.txt')


def street(v):
    queue = []
    visited = [0] * (V+1)  # V: 노드의 개수
    queue.append(v)
    cnt = 0
    while queue:
        new_v = queue.pop(0)
        if new_v == G:  # 도착했을 때
            return distance[new_v]
        elif not visited[new_v]:  # 방문한 적이 없다면
            visited[new_v] = 1  # 방문 처리 (== 현재 노드를 방문했다는 뜻)
            for nb in range(1, V+1):  # nb: 이웃 노드
                # 현재 노드 (new_v)와 연결되어 있고 (G[new_v][nb] == 1)
                # 다음에 방문할 노드 (nb)가 방문한 적이 없다면 (visited[nb] == 0)
                if arr[new_v][nb] == 1 and visited[nb] == 0:
                    if not distance[nb]:
                        distance[nb] = distance[new_v] + 1  # 거리 추가
                    queue.append(nb)
    return 0



T = int(input())
for tc in range(T):
    V , E = map(int, input().split())
    temp = [list(map(int, input().split())) for _ in range(E)]
    S , G = map(int, input().split())
    arr = [[0 for i in range(V+1)] for j in range(V+1)]
    distance = [0] * (V + 1)

    # 인접행렬
    for x in range(len(temp)):
        arr[temp[x][0]][temp[x][1]] = 1
        arr[temp[x][1]][temp[x][0]] = 1  # 방향성이 없는 그래프이므로

    print('#{} {}'.format(tc+1, street(S)))
