import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    adjecent = {key: [] for key in range(1, 1+V)}
    for edge in edges:
        node_start = edge[0]
        node_end = edge[1]
        adjecent[node_start].append(node_end)

    reslut = 0
    stack = [S]
    visited = []
    while stack:
        next_node = stack.pop()
        if next_node == G:
            reslut = 1
            break
        if next_node not in visited:
            visited.append(next_node)
            for nb in adjecent[next_node]:
                stack.append(nb)

    print('#{} {}'.format(tc+1, reslut))
