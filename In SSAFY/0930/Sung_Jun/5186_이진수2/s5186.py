import sys
sys.stdin = open('input.txt')


def change(number):
    result = ''
    i = 1
    while i < 13:
        if number - 2**(-i) > 0:
            number -= 2**(-i)
            result += '1'
            i += 1
        elif number - 2**(-i) < 0:
            result += '0'
            i += 1
        else:
            result += '1'
            return result
    return 'overflow'


T = int(input())
for tc in range(T):
    num = float(input())
    a = change(num)
    print('#{} {}'.format(tc+1, a))
