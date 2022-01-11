import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    result = [0]*5001

    for _ in range(N):
        a, b = map(int, input().split())

        for i in range(a, b+1):
            result[i] += 1

    P = int(input())

    print('#{}'.format(t), end=' ')

    for j in range(P):
        if j == P-1:
            print(result[int(input())])
        else:
            print(result[int(input())], end=' ')