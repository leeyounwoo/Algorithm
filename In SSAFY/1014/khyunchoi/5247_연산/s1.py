import sys
sys.stdin = open('input.txt')


def calc(num, cnt):
    global result

    if num > 1000000 or cnt >= result:
        return

    if num == M:
        result = min(result, cnt)
        return

    calc(num+1, cnt+1)
    calc(num-1, cnt+1)
    calc(num*2, cnt+1)
    calc(num-10, cnt+1)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    result = abs(N-M)
    calc(N, 0)

    print('#{} {}'.format(tc, result))
