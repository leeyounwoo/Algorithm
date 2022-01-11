import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    number_list = list(map(int, input().split()))
    max_sum = 0
    min_sum = 10000 * M

    for i in range(N-M+1):
        prefix_sum = sum(number_list[i:i+M])

        if prefix_sum > max_sum:
            max_sum = prefix_sum
        if prefix_sum < min_sum:
            min_sum = prefix_sum

    print('#{0} {1}'.format(tc+1, max_sum - min_sum))