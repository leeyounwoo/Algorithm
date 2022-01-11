import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    numbers = list(map(int, input().split()))

    first = 0
    while M > 0:
        first = (first+1) % N
        M -= 1

    print('#{} {}'.format(tc, numbers[first]))