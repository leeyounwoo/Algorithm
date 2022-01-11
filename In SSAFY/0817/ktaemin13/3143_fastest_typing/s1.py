import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N, M = map(str, (input().split()))

    result = 0
    cnt = 0

    for i in range(len(N)-len(M)+1):
        if N[cnt:len(M)+cnt] == M:
            result += 1
            cnt = len(M)+cnt - 1
        cnt += 1
    result = len(N) - result*len(M) + result

    print('#{0} {1}'.format(tc+1, result))