import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = input().split()
    len_N = len(N)
    len_M = len(M)
    result = 0
    i = 0

    while i < range(len_N):
        if N[i] == M[0]:
            if N[i:i+len_M] == M:
                i += len_M
                result += 1
            else:
                result += 1
                i += 1
        else:
            result += 1
            i += 1

    print('#{} {}'.format(tc, result))
