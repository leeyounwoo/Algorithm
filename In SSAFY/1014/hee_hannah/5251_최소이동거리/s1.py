import sys
sys.stdin = open('input.txt')

def dijkstra(s):
    distance[s] = 0 # 시작점 0 바꿔주고
    # 노드의 개수만큼 반복 while 써도됨
    for _ in range(N+1):
        # 현재 위치에서 가장 가까운 거리에 있는 노드 찾기
        min_idx = -1
        min_val = float('inf')
        for i in range(N+1):
            if not visited[i] and distance[i] < min_val:
                min_idx = i
                min_val = distance[i]
        visited[min_idx] = 1

        # 해당 노드로부터 인접한 노드들의 거리 살펴보기
        for i in range(N+1):
            if mat[min_idx][i] and not visited[i]: # 연결되어 있고 방문한 적 없는 지 체크
                # 현재 위치까지 오는데 걸린 거리 + 현재 위치부터 i까지 가는데 필요한 거리
                # < (이전에 찾은) i까지 도달하는 최단 경로 -> 바꿔준다
                if distance[min_idx] + mat[min_idx][i] < distance[i]:
                    distance[i] = distance[min_idx] + mat[min_idx][i]

# 프림과 매우 흡사

t = int(input())
for tc in range(1, t+1):
    N, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]

    # 그래프 표현(인접 행렬)
    mat = [[0 for _ in range(N+1)] for _ in range(N+1)] # 인덱스 편하게 하기위해 N+1
    for s, e, w in edges:
        mat[s][e] = w # 방향그래프니까 반대 방향인 [e][s]로 할 필요는 없음
        # 인접리스트를 할때는 s: [e,w] 이렇게 하는듯?

    # 초기화
    distance = [float('inf') for _ in range(N+1)]
    visited = [0] * (N+1)

    # 다익스트라 시작
    start = 0
    dijkstra(start)
    # distance안에 담겼을 테니... N까지 도달하는데 드는 최소 비용 == distance[N]
    print(f'#{tc} {distance[N]}')
    
    # BOJ 다리만들기2 문제 풀어보기~