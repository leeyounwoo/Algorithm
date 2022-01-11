import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    max_num = numbers[0]
    min_num = numbers[0]
    for number in numbers:
        if max_num < number:
            max_num = number

        if min_num > number:
            min_num = number

    print('#{} {}'.format(tc, max_num - min_num))