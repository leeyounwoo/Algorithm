import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    numbers = [2, 3, 5, 7, 11]
    result = ''
    for number in numbers:
        count = 0
        while True:
            if N % number == 0:
                N //= number
                count += 1
            else:
                break
        result += str(count) + ' '

    print('#{} {}'.format(tc+1, result))