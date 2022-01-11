import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for j in range(N):
        tmp = []
        for i in range(N):
            if table[i][j]:
                if len(tmp) == 0 and table[i][j] == 1:
                    tmp.append(table[i][j])
                elif len(tmp) == 1 and table[i][j] == 2:
                    tmp.pop()
                    result += 1

    print('#{} {}'.format(tc, result))