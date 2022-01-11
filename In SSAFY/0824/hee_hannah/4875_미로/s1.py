import sys
sys.stdin = open('input.txt')

def dfs(sy, sx):
    # 핵심 아이디어 : 다음 지점으로 갈때 "필요한 정보를 같이 가져가기"
    stack = [(sy, sx, [])]  # 경로를 저장할 빈 리스트 하나 더( 중요 포인트! 필요한거 하나 더 가져갈수잇다)
    dyx = ((0, 1), (1, 0), (0, -1), (-1, 0))  # 오른쪽 아래 왼쪽 위 순서
    while stack:
        # 현재 방문할 위치
        y, x, path = stack.pop()
        maze[y][x] = 1  # 방문표시
        for dy, dx in dyx: # dyx 안의 방향값을 하나 잡고
            ny, nx = y + dy, x + dx # 이동!
            if 0 <= ny <= N - 1 and 0 <= nx <= N - 1: #범위안에 있을떄
                if maze[ny][nx] == 0: # 방문을 안햇다면
                    stack.append((ny, nx, path + [[y, x]])) # 스택안에 넣어주기
                    if maze[ny][nx] == 3: # 도착점에 왓다면 리턴!
                        return path



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    for i in range(N): # 범위안에 있을때
        for j in range(N):
            if maze[i][j] == 2: # 2라면
                sy, sx = i, j # 초기값 찾기

    result = dfs(sy, sx)
    if result: # result 안에 값이 있다면
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))
