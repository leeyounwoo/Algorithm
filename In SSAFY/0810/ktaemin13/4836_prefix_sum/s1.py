import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N, M = input().split()
    N = int(N)
    M = int(M)
    numbers = input()
    numbers = numbers.split()
    numbers = list(map(int, numbers))


    max = numbers[0]
    min = sum(numbers[:M])

    for cnt in range(N-M+1):
        if sum(numbers[cnt:M+cnt]) > max:
            max = sum(numbers[cnt:M+cnt])

        if sum(numbers[cnt:M+cnt]) < min:
            min = sum(numbers[cnt:M+cnt])

    print('#{0} {1}'.format(tc+1, max - min))