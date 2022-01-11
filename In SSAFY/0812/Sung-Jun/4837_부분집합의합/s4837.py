import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(T):
    a_list = list(range(1, 13))
    len_a = 12
    num, result_sum = map(int, input().split())

    # case1 = []
    # for i in range(1<<len_a):
    #     case2 = []
    #     for j in range(len_a):
    #         if i & (1<<j):
    #             case2.append(a_list[j])
    #     if len(case2) == num:
    #         case1.append(case2)

    # total = 0
    # for sum_list in case1:
    #     number = 0
    #     for num_sum in sum_list:
    #         number += num_sum
    #     if number == result_sum:
    #         total += 1

    case1 = []
    for i in range(1 << len_a):
        case2 = []
        total = 0
        for j in range(len_a):
            if i & (1 << j):
                total += a_list[j]
                case2.append(a_list[j])
        if len(case2) == num and total == result_sum:
            case1.append(case2)


    print('#{} {}'.format(tc+1, len(case1)))

