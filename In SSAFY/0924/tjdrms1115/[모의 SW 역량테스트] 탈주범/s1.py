import sys
sys.stdin = open('input.txt')


def is_border(N, M, i, j):
    if (0 <= i < N) and (0 <= j < M):
        return True
    return False


def is_connected(delta, di, dj, next):
    for next_di, next_dj in delta[next]:
        if -di == next_di and -dj == next_dj:
            return True
    return False


T = int(input())

answer = []
for tc in range(1, T + 1):

    N, M, R, C, L = map(int, input().split())

    tunnel = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0 for _ in range(M)] for _ in range(N)]
    delta = []
    delta.append([])
    delta.append([[0,1], [0,-1], [1,0], [-1,0]])
    delta.append([[1,0], [-1,0]])
    delta.append([[0,1], [0,-1]])
    delta.append([[0,1], [-1,0]])
    delta.append([[0,1], [1,0]])
    delta.append([[0,-1], [1,0]])
    delta.append([[0,-1], [-1,0]])

    queue = []
    queue.append([R, C, 1])

    count = 0
    while queue:
        i, j, t = queue.pop(0)
        if not visited[i][j]:
            visited[i][j] = 1
            count += 1
            for di, dj in delta[tunnel[i][j]]:
                if is_border(N, M, i+di, j+dj) and is_connected(delta, di, dj, tunnel[i+di][j+dj]) and (not visited[i+di][j+dj]) and (t < L):
                    queue.append([i+di, j+dj, t+1])

    result = count
    answer.append(result)

for tc in range(1, T + 1):
    print(f'#{tc} {answer[tc-1]}')