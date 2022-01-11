import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    num = float(input())

    result = ''
    tmp = 0.5
    while num > 0:
        if num >= tmp:
            num -= tmp
            result += '1'
        else:
            result += '0'
        tmp /= 2

        if len(result) > 12:
            result = 'overflow'
            break

    print('#{} {}'.format(tc, result))
