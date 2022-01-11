import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    sum_list = []
    for number in range(N-M+1):
        sum_number = 0
        for num in range(M):
            sum_number += numbers[number+num]
        sum_list.append(sum_number)

    max_num = None
    for number in sum_list:
        if max_num == None:
            max_num = number
        elif max_num < number:
            max_num = number

    min_num = None
    for number in sum_list:
        if min_num == None:
            min_num = number
        elif min_num > number:
            min_num = number
    result = max_num - min_num

    print('#{0} {1}'.format(tc+1, result))