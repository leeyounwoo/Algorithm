import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
    v, e = map(int, input().split())
    temp = []
    edges = [list(map(int, input().split())) for _ in range(e)]
    s, g = map(int, input().split())

    # DFS 시작하기 전에...
    # 그래프 표현 => 인접 행렬 OR 인접 리스트
    adjacent = { key : [] for key in range(1, 1+v)}
    for edge in edges: # [[1, 3], [2, 4]...]
        node_start = edge[0]
        node_end = edge[1]
        adjacent[node_start].append(node_end)

    # DFS 시작
    result = 0
    stack = [s] # 내가 다음에 갈 위치를 저장
    visited = []
    while stack:
        next_node = stack.pop()
        if next_node == g:
            result = 1 # 목표에 도달한 경우 DFS 종료
            break

        if next_node not in visited: # 방문한 적이 없으면
            visited.append(next_node) # 방문 체크
            for nb in adjacent[next_node]:
                stack.append(nb)

    print('#{} {}'.format(tc, result))