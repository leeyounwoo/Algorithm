import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    dump_num = int(input())
    numbers = list(map(int, input().split()))
    len_number = len(numbers)

    while True:
        min_num = max_num = numbers[0]
        min_idx = max_idx = 0
        for number in numbers:
            if min_num > number:
                min_num = number
                min_idx += 1
            if max_num < number:
                max_num = number
                max_idx += 1
        numbers[]
        # max_limt = min_limt = 0
        # for check in range(len_number):
        #     if max_num == numbers[check]:
        #         if max_limt == 0:
        #             numbers[check] -= 1
        #             max_limt += 1
        #     if min_num == numbers[check]:
        #         if min_limt == 0:
        #             numbers[check] += 1
        #             min_limt += 1
        #     if max_limt + min_limt == 2:
        #         break

        dump_num -= 1
        if dump_num < 0:
            break
    print('#{} {}'.format(tc+1,max_num-min_num))