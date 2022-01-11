import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1,T+1):
    V, E = list(map(int, input().split()))
    roads = [list(map(int, input().split())) for _ in range(E)]
    S, G =  map(int, input().split())
    # DFS 시작하기 전에...
    # 그래프 표현 => 인접 행렬 or 인접 리스트
    adjacent = {key: [] for key in range(1, 1+V)}
    for road in roads:
        node_start = road[0]
        node_end =road[1]
        adjacent[node_start].append(node_end)

    # DFS 시작
    result = 0
    stack = [S] # 내가 다음에 갈 위치를 저장
    visited = []
    while stack:
        next_node = stack.pop()
        if next_node == G:
            result = 1 # 목표에 도달한 경우
            break
        if next_node not in visited: # 방문한 적이 없으면
            visited.append(next_node) # 방문 체크
            for nb in adjacent[next_node]:
                stack.append(nb)
    print('#{} {}'.format(test_case, result))

        #
        # for i in range(0, len(road) - 1, 2):
        #     G[road[i]][road[i + 1]] = 1  # 인접한 노드 표기
        #     G[road[i + 1]][road[i]] = 1  # 반대 방향 표기 (무방향 그래프 이므로)
    # for i in range(V + 1):
    #     for j in range(V + 1):
    #         print(G[i][j], end=" ")
    #     print()

