def make_set(x):
    parents[x] = x
    ranks[x] = 0


# find_set
# 어떤 원소 x가 속한 집합의 대표자를 반환하는 함수
def find_set(x):
    if x != parents[x]:
        parents[x] = find_set(parents[x])

    return parents[x]


# union
# 두 개의 상호 배타 집합을 합치는 연산
# 1) 두 집합의 대표자를 찾아서
# 2) 한 쪽의 대표자를 반대쪽의 대표자 바로 밑에 붙입니다.
def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    # root_x의 트리의 높이(rank)가 더 클 경우
    if ranks[root_x] > ranks[root_y]:
        parents[root_y] = root_x
    else:
        parents[root_x] = root_y

        # 만약에 높이가 같아면 rank 증가
        ranks[root_y] += 1


nodes = [1, 2, 3, 4, 5, 6]
parents = [0] * (len(nodes) + 1)  # 각 노드의 부모 저장
ranks = [0] * (len(nodes) + 1)

print(parents)