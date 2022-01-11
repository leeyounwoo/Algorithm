import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    numbers = list(map(int, (input().split())))

    max = 0
    min = 100

    for i in range((N//2)):
        for j in numbers[i*2:N]:
            if j > max:
                max = j
            if j < min:
                min = j

        numbers[i * 2], numbers[numbers.index(max)] = numbers[numbers.index(max)], numbers[i * 2]
        numbers[i * 2 + 1], numbers[numbers.index(min)] = numbers[numbers.index(min)], numbers[i * 2 + 1]

    print('#{0} {1}'.format(tc+1, numbers))