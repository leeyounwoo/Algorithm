import sys
sys.stdin = open('input.txt')


# 시작 위치를 찾습니다.
def find_start(N, board):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                return i, j


# 해당 위치가 적절한지 검사합니다.
def promising(N, maze, i, j):
    if maze[i][j] != 1:
        return True
    return False


# bfs탐색을 통해 길을 찾습니다.
def bfs(N, maze, visited, start_i, start_j):

    # 방향을 알려줄 리스트입니다.
    delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    # 큐로 사용할 리스트입니다. 시작값을 넣고 시작합니다.
    q = []
    q.append([start_i, start_j])
    # bfs 탐색입니다.
    while q:
        # 큐에 저장된 위치를 가져옵니다.
        i, j = q.pop(0)
        # 방문하지 않았다면 방문하고 다음 위치를 찾습니다.
        if not visited[i][j]:
            visited[i][j] = 1
            # 만약 도착점을 찾았다면 1을 반환합니다.
            if maze[i][j] == 3:
                return 1
            # 상하좌우로 탐색하여 적절한 위치가 있다면 큐에 추가합니다.
            for di, dj in delta:
                if promising(N, maze, i+di, j+dj) and not visited[i+di][j+dj]:
                    q.append([i+di, j+dj])
    # 도착점을 찾지 못했다면 0을 반환합니다.
    return 0


# 테스트 케이스의 개수를 입력받습니다. 고정값입니다.
# T = int(input())
T = 10

# 테스트 케이스만큼 코드를 실행하고 결과를 저장합니다.
answer = []
for tc in range(1, T+1):
    # 테스트케이스입니다. 쓰지 않습니다.
    testcase = int(input())
    # N을 입력받습니다. 고정값입니다.
    N = 16
    # 미로를 입력받습니다.
    maze = [list(map(int, input())) for _ in range(N)]

    # 방문 여부를 표시할 배열을 생성합니다.
    visited = [[0 for _ in range(N)] for _ in range(N)]
    # 시작위치를 구합니다.
    start_i, start_j = find_start(N, maze)

    # bfs를 통해 길이 이어져있는지 확인합니다.
    result = bfs(N, maze, visited, start_i, start_j)
    # 결과를 출력합니다.
    answer.append(result)

for tc in range(1, T+1):
    print('#{} {}'.format(tc, answer[tc-1]))
