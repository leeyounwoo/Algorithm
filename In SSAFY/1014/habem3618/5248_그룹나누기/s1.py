import sys
sys.stdin = open('input.txt')


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
    => rank 값이 더 큰 쪽에 붙이기
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


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    parents = [i for i in range(N + 1)]
    ranks = [0] * (N + 1)

    # 주어진 쌍대로 노드 연결
    for i in range(M):
        union(arr[2 * i], arr[2 * i + 1])

    # 부모 노드로 집합의 루트를 설정하도록
    ans = []
    for i in range(1, N + 1):
        ans.append(find_set(i))

    print('#{} {}'.format(tc, len(set(ans))))
