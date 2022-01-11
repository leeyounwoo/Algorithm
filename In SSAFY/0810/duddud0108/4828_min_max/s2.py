import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    number_list = list(map(int, input().split()))
    min_num = min(number_list)
    max_num = max(number_list)

    print('#{0} {1}'.format(tc + 1, max_num - min_num))