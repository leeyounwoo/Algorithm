import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N, Q = map(int, input().split())
    box_list = [0] * N
    for i in range(Q):
        L, R = map(int, input().split())
        box_list[L-1:R] = [i+1] * (R - L + 1)

    print('#{0}'.format(tc+1), *box_list)
