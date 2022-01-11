import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    len_num = input()
    numbers = input()
    check_list = [0]*10

    for number in numbers:
        check_list[int(number)] += 1

    card_num_max = None
    for number in check_list:
        if card_num_max == None:
            card_num_max = number
        elif card_num_max < number:
            card_num_max = number

    index_num = -1
    for check in check_list:
        index_num += 1
        if card_num_max == check:
            result = index_num

    print('#{} {} {}'.format(tc+1, result, card_num_max))