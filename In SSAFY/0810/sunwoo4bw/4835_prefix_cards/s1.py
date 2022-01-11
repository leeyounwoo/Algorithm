import sys

sys.stdin = open('input.txt')

T = int(input())  # 3
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 10, 3
    numbers = list(map(int, input().split()))

    min_sum = 9876543
    max_sum = 0

    # 구간합

    for i in range(N - M + 1):  # i가 0 1 2 3 4 5 6 7
        sum_of_section = 0
        for s in range(i, i + M):  # i가 0일 때 -> 0,1,2
            sum_of_section += numbers[s]

        if max_sum < sum_of_section:
            max_sum = sum_of_section
        if min_sum > sum_of_section:
            min_sum = sum_of_section

    result = max_sum - min_sum

    print('#{} {}'.format(tc, result))