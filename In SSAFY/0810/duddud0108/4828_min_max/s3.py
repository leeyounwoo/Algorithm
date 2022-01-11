import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    number_list = list(map(int, input().split()))
    number_list.sort()
    min_num = number_list[0]
    max_num = number_list[-1]

    print('#{0} {1}'.format(tc + 1, max_num - min_num))