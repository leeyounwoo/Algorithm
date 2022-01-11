import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    for i in range(M):
        numbers.append(numbers.pop(0))

    print('#{} {}'.format(tc, numbers[0]))