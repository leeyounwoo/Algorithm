# import random
import sys

sys.stdin = open('input.txt')
T = int(input())

for test_case in range(1,T+1):
    numbers_number = int(input())
    number_parts = list(map(int, input().split()))
    max_number = number_parts[0]
    min_number = number_parts[0]
    for idx in number_parts:
        if idx > max_number:
            max_number = idx
        if idx < min_number:
            min_number = idx
    print(f'#{test_case} {max_number - min_number}')


