'''
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

def make_set(x):
    parents[x] = x
    ranks[x] = 0


def find_set(x):
    if x != parents[x]:
        parents[x] = find_set(parents[x])

    return parents[x]


def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    # root_x의 트리의 높이(rank)가 더 클 경우
    if ranks[root_x] > ranks[root_y]:
        parents[root_y] = root_x
    # root_y의 트리의 높이가 더 크거나 같을 경우
    else:
        parents[root_x] = root_y
        if ranks[root_x] == ranks[root_y]:
            ranks[root_y] += 1


def find_MST(edges):
    MST = []

    for edge in edges:
        x, y, w = edge
        if find_set(x) != find_set(y):  # Cycle Detection
            # 현재 간선이 MST로 선택 가능하다는 뜻
            MST.append((x, y, w))
            union(x, y)  # MST를 구성하는 부분

    return MST


V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]

parents = [0] * (V + 1)
ranks = [0] * (V + 1)

for v in range(1, 1+V):
    make_set(v)

# 가중치 오름차순으로 정렬
edges.sort(key=lambda x: x[2])
print(find_MST(edges))