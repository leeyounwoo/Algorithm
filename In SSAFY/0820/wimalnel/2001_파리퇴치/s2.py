import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            kill_fly = 0
            for row in range(M):
                for col in range(M):
                    kill_fly += fly[j+col][i+row]

            if kill_fly > result:
                result = kill_fly


    print('#{} {}'.format(tc, result))
