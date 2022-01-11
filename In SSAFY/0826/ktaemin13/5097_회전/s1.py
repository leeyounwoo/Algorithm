import sys
sys.stdin = open('input.txt')


def rotation():
    cnt = 0
    while cnt < M:
        arr.append(arr.pop(0))
        cnt += 1
    return     print('#{} {}'.format(tc+1, *arr))


T = int(input())
for tc in range(T):
    N , M = map(int, input().split())
    arr = list(map(int, input().split()))
    rotation()