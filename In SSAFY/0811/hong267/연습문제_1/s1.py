import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    total = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle)):
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]
                if 0 <= ni < len(puzzle) and 0 <= nj < len(puzzle):
                    total += abs(puzzle[i][j] - puzzle[ni][nj])

    print('#{0} {1}'.format(tc, total))

