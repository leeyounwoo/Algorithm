import sys
sys.stdin = open('input.txt')

def work(i, j, road, flag):
    global answer
    answer = max(answer, road)

    visited[i][j] = 1

    dij = [(1, 0), (0, 1), (-1, 0), (0, -1)]


    for di, dj in dij:
        ni, nj = i+di, j+dj

        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
            if mountain[ni][nj] < mountain[i][j]:
                work(ni, nj, road+1, flag)
            else:                
                if flag:
                    if mountain[ni][nj] - K < mountain[i][j]:
                        temp = mountain[ni][nj]
                        mountain[ni][nj] = mountain[i][j] - 1
                        work(ni, nj, road+1, False)
                        mountain[ni][nj] = temp

    visited[i][j] = 0
    

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())

    mountain = [list(map(int, input().split())) for _ in range(N)]

    # 제일 높은 봉우리 찾기
    max_high = 0
    for i in range(N):
        for j in range(N):
            max_high = max(max_high, mountain[i][j])
    
    visited = [[0 for _ in range(N)] for _ in range(N)]
    answer = 0
    for i in range(N):
        for j in range(N):
            if mountain[i][j] == max_high:
                work(i, j, 1, True)

    print('#{} {}'.format(t, answer))