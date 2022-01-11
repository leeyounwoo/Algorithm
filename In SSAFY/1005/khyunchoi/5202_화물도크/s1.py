import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    time_list = [list(map(int, input().split())) for _ in range(N)]

    time_list.sort(key=lambda x: (x[1], x[0]))

    result = 0
    standard = 0
    for start, end in time_list:
        if start >= standard:
            result += 1
            standard = end

    print('#{} {}'.format(tc, result))