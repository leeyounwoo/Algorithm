import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    case_num = int(input())
    numbers = list(map(int, input().split()))

    max_num = None
    for number in numbers:
        if max_num == None:
            max_num = number
        elif max_num < number:
            max_num = number

    min_num = None
    for number in numbers:
        if min_num == None:
            min_num = number
        elif min_num > number:
            min_num = number
    result = max_num - min_num
    print('#{0} {1}'.format(tc+1, result))