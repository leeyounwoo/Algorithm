import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1) :
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    total = 0
    for number in numbers[:M] :
        total += number

    max_sum = min_sum = total
    i = 0
    while M+i < N :
        total -= numbers[i]
        total += numbers[M+i]

        if total < min_sum :
            min_sum = total
        elif total > max_sum :
            max_sum = total

        i += 1

    print(f'#{t} {max_sum-min_sum}')