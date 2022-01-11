import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
    n, q = map(int, input().split())
    value = [0] * n

    for i in range(1, q+1):
        l, r = map(int, input().split())

        for j in range(l-1, r):
            value[j] = i

    result = ''
    for i in value:
        result += str(i) + ' '

    print('#{0} {1}'.format(tc, result))