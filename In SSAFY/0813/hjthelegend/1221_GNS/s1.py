import sys
sys.stdin = open('input.txt')

new_numbers = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

t = int(input())

for _ in range(t):
    order, test_number = input().split()
    numbers_input = list(input().split())

    answer = []

    for i in new_numbers:
        for j in numbers_input:
            if j == i:
                answer.append(j)

    print(order)
    print(' '.join(answer))



