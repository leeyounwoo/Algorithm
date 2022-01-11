import sys
sys.stdin = open('input.txt')

for _ in range(10):
    T = int(input())
    number_list = list(map(int, input().split()))

    i = 0
    while number_list[-1] > 0:
        num = number_list.pop(0)
        number_list.append(num-(i % 5 + 1))  # 1 2 3 4 5 가 반복되므로
        i += 1
    number_list[-1] = 0

    print('#{}'.format(T), *number_list)