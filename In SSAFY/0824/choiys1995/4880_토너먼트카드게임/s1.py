import sys
sys.stdin = open('input.txt')


def rps(a, b):
    if students[a] == 1 and students[b] == 2:
        return b
    elif students[a] == 2 and students[b] == 3:
        return b
    elif students[a] == 3 and students[b] == 1:
        return b
    else:
        return a


def tournament(start, end):
    if start == end:
        return start

    return rps(tournament(start, (start+end)//2), tournament((start+end)//2 + 1, end))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    students = list(map(int, input().split()))

    result = tournament(0, N-1) + 1
    print('#{} {}'.format(tc, result))