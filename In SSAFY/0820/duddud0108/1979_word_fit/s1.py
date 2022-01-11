import sys
sys.stdin = open('input.txt')

def rotate(N, matrix):
    matrix90 = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            matrix90[j][N - 1 - i] = matrix[i][j]

    return matrix90

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())

    puzzle = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    for _ in range(2):
        for i in range(N):
            # 행을 검사
            cnt_r = 0
            for j in range(N):
                if puzzle[i][j] == 1:
                    cnt_r += 1
                else:
                    if cnt_r == K:
                        answer += 1
                    cnt_r = 0

            if cnt_r == K:
                answer += 1

        puzzle = rotate(N, puzzle)
    print('#{} {}'.format(tc + 1, answer))