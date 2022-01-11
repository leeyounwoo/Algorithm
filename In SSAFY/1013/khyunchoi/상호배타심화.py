def make_set(x):
    parents[x] = x
    ranks[x] = 0


def find_set(x):
    """
    path compression 적용
    => 부모 노드를 루트 노드로 갱신
    """
    if x != parents[x]:
        parents[x] = find_set(parents[x])

    return parents[x]


def union(x, y):
    """
    union by rank 적용
    => rank 갑이 더 큰 쪽에 붙이기
    """
    root_x = find_set(x)
    root_y = find_set(y)

    # root_x의 트리의 높이(rank)가 더 클 경우
    if ranks[root_x] > ranks[root_y]:
        parents[root_y] = root_x
    # root_y의 트리의 높이가 더 크거나, 혹은 둘이 같을 경우
    else:
        parents[root_x] = root_y
        # 만약에 높이가 같다면 rank 증가
        if ranks[root_x] == ranks[root_y]:
            ranks[root_y] += 1


nodes = [1, 2, 3, 4, 5, 6]
parents = [0] * (len(nodes) + 1)  # 각 노드의 부모 저장
ranks = [0] * (len(nodes) + 1)
