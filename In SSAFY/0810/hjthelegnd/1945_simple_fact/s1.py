import sys
sys.stdin = open('input.txt')

t = int(input())
numbers = [2, 3, 5, 7, 11]

for tc in range(1, t+1):
    n = int(input())

    result = ''
    for i in numbers:
        count = 0

        while n % i == 0:
            n /= i
            count += 1

        result += str(count) + ' '

    print('#{0} {1}'.format(tc, result))