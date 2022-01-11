import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    count = input()
    numbers = list(map(int, input().split()))

    max, min = numbers[0], numbers[0]

    for number in numbers:
        if number > max:
            max = number
        if number < min:
            min = number

    print('#{0} {1}'.format(tc+1,max-min))