import sys
sys.stdin = open('input.txt')

def bfs(start, end):
    queue = []
    queue.append(start)
    visited[start] = 1
    while queue:
        v = queue.pop(0)
        for w in node[v]: # 인접한 노드
            if not visited[w]:
                # 방문처리
                visited[w] = 1
                # 거리설정
                distance[w] = distance[v] + 1
                queue.append(w)
                # 도착지점에 도착했으면
                if w == end:
                    # 거리를 반환
                    return distance[w]
    return 0

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())

    node = [[] for _ in range(V + 1)]
    # 방향이 없는 그래프
    for i in range(E):
        u, v = map(int, input().split())
        node[u].append(v)
        node[v].append(u)
    start, end = map(int, input().split())

    visited = [0] * (V + 1) # 방문 여부
    distance = [0] * (V + 1) # 번호별 도달 거리


    print('#{} {}'.format(tc, bfs(start, end)))
