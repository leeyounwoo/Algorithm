import sys
sys.stdin = open('input.txt')

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def find():
    inf = 10000000
    dist = [[inf] * N for i in range(N)]
    dist[0][0] = 0 # 시작값
    # 상하좌우 탐색 -> 다시 상하좌우 탐색
    q = []
    q.append((0, 0))
    while q:
        t = q.pop()
        for i in range(4):
            nr = t[0] + dr[i]
            nc = t[1] + dc[i]
            if nr >= 0 and nr < N and nc >= 0 and nc < N:
                dis = 0
                # 현재 위치와 새 위치 높이 차이 구하기
                if lst[nr][nc] > lst[t[0]][t[1]]:
                    dis = lst[nr][nc] - lst[t[0]][t[1]]
                # 최단 거리 = 현재 위치에서 최단거리 + 높이차 + 1
                if dist[nr][nc] > dist[t[0]][t[1]] + dis + 1:
                    dist[nr][nc] = dist[t[0]][t[1]] + dis + 1
                    q.append((nr, nc))
    # 도착점 값 리턴
    return dist[N-1][N-1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    print('#{} {}'.format(tc, find()))