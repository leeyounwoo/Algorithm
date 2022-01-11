import sys
sys.stdin = open('input.txt')

T =int(input())

for tc in range(T):
    len_number = int(input())
    number = list(map(int, input().split()))

    for i in range(len_number-1):
        if i == 10:
            break
        for j in range(i+1, len_number):
            if i % 2 == 0:
                if number[i] < number[j]:
                    number[i], number[j] = number[j], number[i]
            else:
                if number[i] > number[j]:
                    number[i], number[j] = number[j], number[i]
    print(number[:10])