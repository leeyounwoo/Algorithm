import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(T):
    case_number = input()
    arr_size = 100
    numbers = [list(map(int, input().split())) for _ in range(arr_size)]

    result = []
    for i in range(arr_size):
        total = 0
        for j in range(arr_size):
            total += numbers[i][j]
        result.append(total)

    for j in range(arr_size):
        total = 0
        for i in range(arr_size):
            total += numbers[i][j]
        result.append(total)

    for i in range(arr_size):
        total = 0
        for j in range(arr_size):
            if j == i:
                total += numbers[i][j]
        result.append(total)

    for i in range(arr_size):
        total = 0
        for j in range(arr_size):
            if i+j+1 == arr_size:
                total += numbers[i][j]
        result.append(total)

    max_num = result[0]
    for mx in result:
        if max_num < mx:
            max_num = mx
    print('#{} {}' .format(tc+1, max_num))