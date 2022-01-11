import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(T):
    N = int(input())
    case = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for j in range(N):
        flag = 0
        for i in range(N):
            if flag == 0 and case[i][j] == 1:
                flag = 1
            elif flag == 1 and case[i][j] == 2:
                cnt += 1
                flag = 0
    print('#{} {}'.format(tc+1, cnt))


