# 인접 리스트

T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    edges = list(map(int, input().split()))
    S, G = map(int, input().split())

    # 인접 리스트
    adjacent = {key: [] for key in range(1, 1+V)}
    for edge in edges:
        node_start = edge[0]
        node_end = edge[1]
        adjacent[node_start].append(node_end)

    # DFS 시작
    result = 0
    stack = [S] # 내가 다음에 갈 위치를 지정
    visited = []
    while stack:
        next_node = stack.pop()
    if next_node == G:
        result = 1
        break
        if next_node not in visited:
            visited.append(next_node)
            for nb in adjacent[next_node]:
                stack.append(nb)

    print("#{} {}").format(tc + 1 , result)