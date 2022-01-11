import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    n_max = numbers[0]
    n_min = numbers[0]
    for i in numbers:
        if i > n_max:
            n_max = i
        if i < n_min:
            n_min = i
    result = (n_max - n_min)

    print('#{} {}'.format(tc, result))

