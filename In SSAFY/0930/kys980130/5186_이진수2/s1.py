import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = float(input())
    base = 1/2
    result = ''
    for i in range(12):
        if N - base >= 0:
            result += '1'
            N -= base
            base *= 1/2
        else:
            result += '0'
            base *= 1/2
        if N == 0:
            break
    if N:
        result = 'overflow'
    print('#{} {}'.format(tc, result))

