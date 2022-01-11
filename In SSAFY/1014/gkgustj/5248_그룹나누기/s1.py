import sys
sys.stdin = open('input.txt')

def find_set(x):
    if x != parents[x]:
        parents[x] = find_set(parents[x])

    return parents[x]


def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    # root_x의 트리의 높이가 더 크거나 같을 경우
    if ranks[root_x] >= ranks[root_y]:
        parents[root_y] = root_x
        # 만약에 높이가 같다면 rank 증가
        if ranks[root_x] == ranks[root_y]:
            ranks[root_y] += 1
    # root_y의 트리의 높이가 더 클 경우
    else:
        parents[root_x] = root_y


T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    paper = list(map(int, input().split()))

    parents = [x for x in range(N+1)]
    ranks = [0 for _ in range(N+1)]

    for i in range(0, M*2-1, 2):
        union(paper[i], paper[i+1])
    
    for j in range(1, N+1):
        find_set(j)

    print('#{} {}'.format(t, len(set(parents))-1))