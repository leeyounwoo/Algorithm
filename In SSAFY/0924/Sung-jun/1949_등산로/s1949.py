import sys
sys.stdin = open('input.txt')
'''
가장 높은산 찾기
델타 탐색으로 위치 검사하고 다음 위치산이 높낮이 평가
위치 이동시 방문지 등록을 통해 재 방문 방지(공사 가능하므로)
만약 높다면 공사 했을시 가능한지 검토 
처음 으로돌아갈시 변동사항 및 방문 여부 다시 초기화
마지막에 이제까지의 길이를 저장
'''

def mountain(now_y, now_x, road, k):
    global ans
    visited[now_y][now_x] = 1
    if ans < road:
        ans = road
    for i in range(4):
        ny = now_y + dy[i]
        nx = now_x + dx[i]

        if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
            if case[now_y][now_x] > case[ny][nx]:
                mountain(ny, nx, road+1, k)
            elif case[now_y][now_x] > case[ny][nx] - K and k:
                temp = case[ny][nx]
                case[ny][nx] = case[now_y][now_x] - 1
                mountain(ny, nx, road+1, 0)
                case[ny][nx] = temp

    visited[now_y][now_x] = 0


def case_location(case):
    num_max = 0
    case_max = []
    for i in range(N):
        for j in range(N):
            if num_max < case[i][j]:
                case_max = []
                num_max = case[i][j]
                case_max.append([i, j])
            elif num_max == case[i][j]:
                case_max.append([i, j])
    return case_max


T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    case = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    ans = 0
    start_location = case_location(case)
    for now_y, now_x in start_location:
        mountain(now_y, now_x, 1, 1)

    print('#{} {}'.format(tc+1, ans))


