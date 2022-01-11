import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    max_prefix_sum = numbers[0]
    min_prefix_sum = 1000000
    # min_prefix_sum = 0
    # for number in numbers:
    #     min_prefix_sum += number

    for i in range(N-M+1): # 0부터 N-M까지
        prefix_sum = 0
        for j in range(i, i+M): # i부터 M개
            prefix_sum += numbers[j]

        if max_prefix_sum < prefix_sum:
            max_prefix_sum = prefix_sum

        if min_prefix_sum > prefix_sum:
            min_prefix_sum = prefix_sum

    result = max_prefix_sum - min_prefix_sum

    print('#{} {}'.format(tc, result))