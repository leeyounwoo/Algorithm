import sys
sys.stdin = open('input.txt')


INF = 100000000


def is_possible(N, i, j):
    if (0 <= i < N) and (0 <= j < N):
        return True
    return False


delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def dijkstra(N, board):
    D = [[INF for _ in range(N)] for _ in range(N)]
    D[0][0] = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]

    candidates = set([(0, 0)])
    for _ in range(N * N):
        min_dist = INF
        checklist = []
        vi, vj = -1, -1
        for i, j in candidates:
            if not visited[i][j] and min_dist > D[i][j]:
                min_dist = D[i][j]
                vi, vj = i, j
            elif visited[i][j]:
                checklist.append((i, j))

        for i, j in checklist:
            candidates.remove((i, j))

        visited[vi][vj] = 1

        for di, dj in delta:
            if is_possible(N, vi + di, vj + dj) and not visited[vi + di][vj + dj]:
                candidates.add((vi + di, vj + dj))
                if D[vi + di][vj + dj] > D[vi][vj] + board[vi + di][vj + dj]:
                    D[vi + di][vj + dj] = D[vi][vj] + board[vi + di][vj + dj]

    return D[N - 1][N - 1]


T = int(input())

answer = []
for tc in range(1, T + 1):
    N = int(input())

    board = [list(map(int, input())) for _ in range(N)]

    result = dijkstra(N, board)

    answer.append(result)

for tc in range(1, T + 1):
    print(f'#{tc} {answer[tc-1]}')

