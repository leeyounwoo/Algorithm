import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    P, A, B = map(int, input().split())

    a_cnt = 0
    b_cnt = 0

    for target in (A, B):
        l = 1
        r = P
        c = (l + r) // 2

        cnt = 1
        while target != c:
            if target < c:
                r = c
            else:
                l = c

            c = (l + r) // 2
            cnt += 1

        if target == A:
            a_cnt = cnt
        else:
            b_cnt = cnt

    if a_cnt > b_cnt:
        print('#{} B'.format(t))
    elif a_cnt == b_cnt:
        print('#{} 0'.format(t))
    else:
        print('#{} A'.format(t))