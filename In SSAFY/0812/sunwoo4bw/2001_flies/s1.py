import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 5 2

    flies_board = [list(map(int, input().split())) for _ in range(N)]
    # [1, 3, 3, 6, 7]
    # for _ in range(N):  # N을 반복해서

    killed_max = 0
    # second tc
    for i in range(0, N - M + 1):  # 0 1 2 3
        for j in range(0, N - M + 1):
            tmp = 0
            for x in range(i, i + M):  # i가 0일 때, 0, 3 -> 0 1 2/ i가 1일 때, 1, 4 -> 1,2,3/ 3일 때, 3, 6 -> 3 4 5
                for y in range(j, j + M):
                    sum_killed_flies = flies_board[x][y]
                    tmp += sum_killed_flies

                    if killed_max < tmp:
                        killed_max = tmp

    print('#{} {}'.format(tc, killed_max))