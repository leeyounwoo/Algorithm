import sys
sys.stdin = open('input.txt')
# 가중치 없고 무방향

def max_length(idx, cnt):
    global length
    # 방문 처리
    visited[idx] = 1
    # 최댓값
    if length < cnt:
        length = cnt
    # 이웃 노드 탐색
    for j in range(1, N + 1): # 1/ 1 2 3
        #if adj_mat[idx][j] == 1 and visited[j] == 0:
        if adj_mat[idx][j] and not visited[j]: # 나랑 연결된 node가 있고 지금 가려고 하는 node가 방문된 적이 없다면,
            max_length(j, cnt + 1)

    visited[idx] = 0

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 정점, 간선의 수
    adj_mat = [[0] * (N + 1) for _ in range(N + 1)]
    visited = [0] * (N + 1)

    # 인접행렬
    for _ in range(M):
        x, y = map(int, input().split()) # x,y 간선 정보
        adj_mat[x][y] = 1
        adj_mat[y][x] = 1 # 무방향이니까 거꾸로도

    length = 0 # 최댓값 구하는 거
    for i in range(1, N + 1): # 1/ 1 2 3
        max_length(i, 1)

    print('#{} {}'.format(tc, length))