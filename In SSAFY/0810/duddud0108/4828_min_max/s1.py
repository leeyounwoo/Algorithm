import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    number_list = list(map(int, input().split()))
    min_num, max_num = number_list[0], number_list[0]

    for i in range(1, N):
        if number_list[i] > max_num:
            max_num = number_list[i]
        if number_list[i] < min_num:
            min_num = number_list[i]

    print('#{0} {1}'.format(tc+1, max_num - min_num))

