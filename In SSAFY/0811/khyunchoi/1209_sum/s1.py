import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    my_list = []
    for _ in range(100):
        my_list.append(list(map(int, input().split())))

    max_result = 0
    for i in range(100):
        result = 0
        for j in range(100):
            result += my_list[i][j]

        max_result = max(max_result, result)

    for i in range(100):
        result = 0
        for j in range(100):
            result += my_list[j][i]

        max_result = max(max_result, result)

    result_cross1 = 0
    result_cross2 = 0
    for i in range(100):
        result_cross1 += my_list[i][i]
        result_cross2 += my_list[i][99 - i]

    max_result = max(max(max_result, result_cross1), result_cross2)

    print('#{} {}'.format(tc, max_result))