from copy import deepcopy
dxy = [(0,1), (1,0), (0,-1), (-1,0)]
sys.stdin = open('input.txt')

def move_block(matrix):
    map = [[0 for _ in range(W)] for _ in range(H)]
    for i in range(W):
        stack = []
        for j in range(H):
            if matrix[j][i]:
                stack.append(matrix[j][i])

        for k in range(len(stack)):
            map[H - len(stack) + k][i] = stack[k]
    return map

def breaker(n, matrix, block_cnt):
    global ans

    if n == N or block_cnt == 0:
        ans = min(ans, block_cnt)
        return

    for i in range(W):
        for j in range(H):
            if matrix[j][i] > 0:
                matrix_copy = deepcopy(matrix)
                cnt = block_cnt - 1
                stack = [(j, i, matrix_copy[j][i])]
                matrix_copy[j][i] = 0

                while stack:
                    x, y, m = stack.pop()

                    for dx, dy in dxy:
                        for c in range(1, m):
                            nx, ny = x + dx * c, y + dy * c

                            if -1 < nx < H and -1 < ny < W and matrix_copy[nx][ny]:
                                if matrix_copy[nx][ny] > 1:
                                    stack.append((nx, ny, matrix_copy[nx][ny]))
                                matrix_copy[nx][ny] = 0

                final_matrix = move_block(matrix_copy)
                breaker(n + 1, final_matrix, cnt)
                break

T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(H)]
    numbers = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j]:
                numbers += 1
    ans = 999999
    breaker(0, matrix, numbers)
    print('#{} {}'.format(tc, ans))
