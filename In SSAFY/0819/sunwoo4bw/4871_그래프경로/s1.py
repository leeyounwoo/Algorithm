# 1. 인풋값 받아서 인접행렬로 그래프 만들기
# 2. 시작점부터 DFS 실행
# 3. 다음에 방문할 노드가 목표지점(G)일 경우 1을 정답으로 반환
# 4. DFS가 끝나버리면(시작점부터 모든 지점을 다 방문했음에도)
# 목표지점과 연결되어 있지 않다는 뜻이므로 정답으로 0을 반환
import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):  # 3만큼 돌
    V, E = map(int, input().split())  # 6, 5 받

    # edges = [] # [[1,4]. [2,4]   ]
    # for _ in range(E):  # 간선의 개수만큼 돌아서 input값 받아줘
    #     edges.append(list(map(int,input().split())))
    edges = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    # DFS 시작하기 전에
    # 그래프 표현 => 인접 행렬 or 인접 리스트(딕셔너리를 주로 씀)
    # 인접 리스트로 해보자!
    adjacent = {key: [] for key in range(1, 1 + V)}
    for edge in edges:  # [ [1,3], [2,4] ...]
        node_start = edge[0]
        node_end = edge[1]
        adjacent[node_start].append(node_end)  # 키가 node_start
    # DFS 시작
    result = 0  # 일단 경로 없음으로 초기화
    stack = [S]  # 내가 다음에 갈 위치를 저장
    visited = []
    while stack:
        next_node = stack.pop()
        if next_node == G :
            result = 1 # 목표에 도달한 경우 - DFS 종료
            break

        if next_node not in visited:  # 방문한 적이 없으면
            visited.append(next_node)  # 방문 체크
            for nb in adjacent[next_node]:
                stack.append(nb)

    print('#{} {}'.format(tc, result))