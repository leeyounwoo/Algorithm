import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    N = int(input())//10

    memo = [1, 3]

    if N > 2:
        for i in range(2, N):
            memo.append(memo[i-1] + memo[i-2]*2)

    print('#{} {}'.format(t, memo[N-1]))