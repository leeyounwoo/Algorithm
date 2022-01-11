import sys

sys.stdin = open('input.txt')
for T in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))

    sum_list = []
    for i in range(n - m + 1):
        temp_sum = 0
        for j in range(i, i + m):
            temp_sum += numbers[j]
        sum_list.append(temp_sum)

    max_sum = sum_list[0]
    min_sum = sum_list[0]
    for i in range(len(sum_list)):
        if max_sum < sum_list[i]:
            max_sum = sum_list[i]
        if min_sum > sum_list[i]:
            min_sum = sum_list[i]

    print('#{} {}'.format(T, max_sum - min_sum))
