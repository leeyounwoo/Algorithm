import sys
sys.stdin = open('input.txt')

def find_set(x):
    while p[x] != x:
        x = p[x]
    return x
def union(x,y):
    p[find_set(y)] = find_set(x)
# Kruskal -> 가장 먼저 가중치 오름차순 정렬, 간선의 배열 이용할 것, 간선을 선택하는 것! (<-> prim은 정점)
# 간선은 정점 -1
T = int(input())
for tc in range(1, T +1):
    V, E = map(int, input().split()) # V: 정점의 마지막 번호!(0번 부터 시작), 정점의 개수는 V+1
    edges = [list(map(int, input().split())) for _ in range(E)]
    # 가중치 정렬
    edges.sort(key=lambda x:x[2])

    # 람다 모르면?
    # edges = []
    # for _ in range(E):
    #     n1, n2, w = map(int, input().split())
    #     edges.append((w, n1, n2)) # 받을 때 반대로 받으면 되겠네!
    # edges.sort()

    p = list(range(V+1)) # make-set
    cnt = 0 # 간선을 선택한 횟수
    ans = 0 # 가중치를 더한 값
    idx = 0 # edges 인덱스

    while cnt < V :
        n1 = edges[idx][0]
        n2 = edges[idx][1]

        if find_set(n1) != find_set(n2): # 대표를 찾았을 때 서로 다르다면,
            union(n1, n2)
            cnt += 1
            ans += edges[idx][2] # 각각 가중치 더하기

        idx += 1 # 다음 간선 배열을 위해 인덱스 하나 증가
    print('#{} {}'.format(tc, ans))
