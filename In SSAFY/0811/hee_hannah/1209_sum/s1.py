import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, 11):
    a = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    sum_numbers = []

    for i in range(100):
        total1 = 0
        for j in range(100):
            total1 += arr[i][j]
        sum_numbers.append(total1)

    for i in range(100):
        total2 = 0
        for j in range(100):
            total2 += arr[j][i]
        sum_numbers.append(total2)

    total3 = 0
    for i in range(100):
        total3 += arr[i][i]
    sum_numbers.append(total3)

    total4 = 0
    for i in range(100):
        total4 += arr[i][4-i]
    sum_numbers.append(total4)

    max_num = sum_numbers[0]
    for k in sum_numbers:
        if k > max_num:
            max_num = k

    print('#{} {}'.format(tc, max_num))
