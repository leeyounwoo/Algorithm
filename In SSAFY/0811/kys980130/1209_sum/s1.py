import sys
sys.stdin = open("input.txt")
for tc in range(10):
    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(100)]
    result = []

    for j in range(len(numbers)):
        total_row = 0
        for i in range(len(numbers)):
            total_row += numbers[j][i]
            result.append(total_row)

    for i in range(len(numbers)):
        total_col = 0
        for j in range(len(numbers)):
            total_col += numbers[i][j]
            result.append(total_col)


    for i in range(len(numbers)):
        total_1 = 0
        total_1 += numbers[i][i]
        result.append(total_1)


    for i in range(len(numbers)):
        total_2 = 0
        total_2 += numbers[i][len(numbers)-i-1]
        result.append(total_2)

    max_num = 0
    for number in result:
        if number > max_num:
            max_num = number
    print(max_num)


