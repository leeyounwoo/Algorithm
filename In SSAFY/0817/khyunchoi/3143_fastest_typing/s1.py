import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    a, b = input().split()

    new_a = a.replace(b, '0')
    result = len(new_a)

    print('#{} {}'.format(tc, result))