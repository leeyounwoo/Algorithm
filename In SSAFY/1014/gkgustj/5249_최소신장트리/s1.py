import sys
sys.stdin = open('input.txt')

def find_set(x):
    if x != parents[x]:
        parents[x] = find_set(parents[x])

    return parents[x]


def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    # root_x의 트리의 높이(rank)가 더 클 경우
    if ranks[root_x] >= ranks[root_y]:
        parents[root_y] = root_x
        # 만약에 높이가 같다면 rank 증가
        if ranks[root_x] == ranks[root_y]:
            ranks[root_y] += 1
    # root_y의 트리의 높이가 더 크거나 같을 경우
    else:
        parents[root_x] = root_y


def mst(edges):
    total = 0
    mst_list = []

    for n1, n2, w in edges:
        if find_set(n1) != find_set(n2):
            mst_list.append((n1, n2, w))
            union(n1, n2)
            total += w

    return total
    

T = int(input())

for t in range(1, T+1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    
    parents = [x for x in range(V+1)]
    ranks = [0 for _ in range(V+1)]

    edges.sort(key=lambda x: x[2])
    print('#{} {}'.format(t, mst(edges)))