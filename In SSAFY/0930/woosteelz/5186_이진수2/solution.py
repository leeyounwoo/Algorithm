import sys
sys.stdin = open('0930/woosteelz/5186_이진수2/input.txt')

TC = int(input())
for tc in range(1, TC + 1):
    N = float(input())
    ans = ''

    while N:
        N *= 2
        if N >= 1:
            ans += '1'
            N -= 1
        else:
            ans += '0'

    if len(ans) > 12:
        ans = 'overflow'

    print(f"#{tc} {ans}")
