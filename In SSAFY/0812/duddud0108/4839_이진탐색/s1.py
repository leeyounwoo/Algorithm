import sys
sys.stdin = open('input.txt')

def binary_search(r, a, b):
    a_start = b_start = 1
    a_end = b_end = r

    while True:
        a_middle = (a_start + a_end)//2
        b_middle = (b_start + b_end)//2

        if a == a_middle and b == b_middle:
            return 0
        elif a == a_middle:
            return 'A'
        elif b == b_middle:
            return 'B'

        if a_middle > a:
            a_end = a_middle
        else:
            a_start = a_middle

        if b_middle > b:
            b_end = b_middle
        else:
            b_start = b_middle

T = int(input())

for tc in range(T):
    r, a ,b = map(int, input().split())
    print('#{0} {1}'.format(tc+1, binary_search(r, a, b)))