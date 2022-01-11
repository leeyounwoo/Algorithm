import sys
sys.stdin = open('input.txt')


def longest(idx, cnt):
    global temp
    # 방문 처리
    visited[idx] = 1
    # 최댓값
    if temp < cnt:
        temp = cnt # 1
    # 이웃 노드 탐색
    for j in range(1, N + 1):

        if mat[idx][j] and not visited[j]: # 인접 node 노드이고 방문된 적이 없다면,
            longest(j, cnt + 1)

    visited[idx] = 0


t = int(input())
for tc in range(1, t + 1):
    N, M = map(int, input().split())  # 정점, 간선의 수
    mat = [[0] * (N + 1) for _ in range(N + 1)]
    visited = [0] * (N + 1)

    # adjacent matrix
    for _ in range(M):
        s, e = map(int, input().split()) # x,y 간선 정보
        mat[s][e] = 1
        mat[e][s] = 1 # 무방향
    #print(mat)  # [[0, 0], [0, 0]]

    temp = 0
    for i in range(1, N + 1): # 정점마다
        longest(i, 1)

    print('#{} {}'.format(tc, temp))