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
    if (0 <= i < N) and (0 <= j < N) and (maze[i][j]) != 1:
        return True
    return False


# bfs탐색을 통해 길을 찾습니다.
def bfs(N, maze, visited, start_i, start_j):
    # 방향을 알려줄 리스트입니다.
    delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    # 거리를 저장할 변수를 생성합니다.
    distance = 0
    # 큐로 사용할 리스트입니다. 시작값을 넣고 시작합니다.
    q = []
    q.append([start_i, start_j])
    # bfs 탐색입니다.
    while q:
        # 현재 큐에 저장되어 있는 만큼만 경로 찾기를 반복합니다.
        # while문 반복 한 번에 들어가는 노드들은
        # 같은 거리를 공유합니다.
        cur_item_num = len(q)
        for _ in range(cur_item_num):
            # 큐에 저장된 위치를 가져옵니다.
            i, j = q.pop(0)
            # 방문하지 않았다면 방문하고 다음 위치를 찾습니다.
            if not visited[i][j]:
                visited[i][j] = 1
                # 만약 도착점을 찾았다면 거리를 반환합니다.
                if maze[i][j] == 3:
                    return distance-1
                # 상하좌우로 탐색하여 적절한 위치가 있다면 큐에 추가합니다.
                for di, dj in delta:
                    if promising(N, maze, i+di, j+dj) and not visited[i+di][j+dj]:
                        q.append([i+di, j+dj])
        # 거리를 갱신합니다.
        distance += 1
    # 도착점을 찾지 못했다면 0을 반환합니다.
    return 0


# 테스트 케이스의 개수를 입력받습니다.
T = int(input())

# 테스트 케이스만큼 코드를 실행하고 결과를 저장합니다.
answer = []
for tc in range(1, T+1):

    # 입력값을 입력받습니다.
    N = int(input())
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
