import sys
sys.stdin = open('input.txt')

def my_max(numbers):
    test = -9999
    for number in numbers:
        if test < number:
            test = number
    return test

T = 10

for tc in range(1, T+1):
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    result = []
    for i in range(100):
        total_1 = 0
        for j in range(100):
            total_1 += arr[i][j]
        result.append(total_1)

    for i in range(100):
        total_2 = 0
        for j in range(100):
            total_2 += arr[j][i]
        result.append(total_2)


    total = my_max(result)
    print('#{} {}'.format(tc, total))