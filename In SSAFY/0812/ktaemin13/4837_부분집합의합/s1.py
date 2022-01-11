import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N, M = input().split()

    result = 0
    A = list(range(1, 13))
    if M > N(N+1) / 2:
        result = 0




    print('#{0} {1}'.format(tc+1, result))