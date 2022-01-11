import sys

sys.stdin = open('input.txt')

for T in range(1, int(input()) + 1):

    n, m = map(int, input().split())
    temp_list = list(map(int, input().split()))
    sum_list = []
    for i in range(n - m + 1):
        temp_sum = 0
        for j in range(m):
            temp_sum += temp_list[i + j]
        sum_list.append(temp_sum)
    ans = (max(sum_list) - min(sum_list))

    print('#{} {}'.format(T, ans))