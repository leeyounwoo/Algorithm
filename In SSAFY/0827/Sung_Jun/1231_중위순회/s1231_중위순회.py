import sys
sys.stdin = open('input.txt')


def in_order(n):
    if n:
        in_order(left[n])
        print(node[n], end='')
        in_order(right[n])


T = 10
for tc in range(T):
    N = int(input())
    node = [''] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)
    case_box = [list(map(str, input().split())) for _ in range(N)]

    for case in case_box:
        node[int(case[0])] = case[1]
        if len(case) > 2:
            left[int(case[0])] = int(case[2])
            if len(case) > 3:
                right[int(case[0])] = int(case[3])

    print('#{}'.format(tc+1), end=' ')
    in_order(1)
    print()





