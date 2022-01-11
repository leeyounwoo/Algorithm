import sys
sys.stdin = open('input.txt')

def dfs(sy, sx):

    global ans
    stack = [(sy, sx)]
    dyx = ((0, 1), (0, -1), (1, 0), (-1, 0)) # 오른쪽, 아래, 왼쪽, 위쪽 순서

    while stack:
        sy, sx = stack.pop()
        maze[sy][sx] = 1  # 방문 체크
        # 현재 위치(y, x)에서 갈 수 있는 곳 탐색
        for dy, dx in dyx:
            ny, nx = sy + dy, sx + dx
            # 범위를 벗어난 길이면 다음 길 연산
            if ny < 0 or nx < 0 or ny >= N or nx >= N:
                continue
            # 3이면 도착지점
            if maze[ny][nx] == 3:
                ans = 1
                break
            # 0이면 스택에 추가
            elif maze[ny][nx] == 0:
                stack.append((ny, nx))
        # break 되지 않았다면 다음 연산으로
        else:
            continue
        # break 되었다면(답이 나왔다면 반복 종료)
        break

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)]
    sy, sx = 0, 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sy, sx = i, j
                break
    ans = 0
    dfs(sy, sx)
    print('#{} {}'.format(tc, ans))