import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    num = float(input())
    n = -1
    answer = ''
    while num > 0:
        if n == -13:
            answer = 'overflow'
            break
        if num >= 2**n:
            num -= 2**n
            answer += '1'
        else:
            answer += '0'
        n -= 1
    print('#{} {}'.format(tc, answer))

