import sys
sys.stdin = open('input.txt')

TC = int(input())
for tc in range(TC):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]

    max_kill = 0

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            kill = 0
            for x in range(i, i + M):
                for y in range(j, j + M):
                    kill += flies[x][y]
            if kill > max_kill:
                max_kill = kill

    print('#{} {}'.format(tc+1, max_kill))
