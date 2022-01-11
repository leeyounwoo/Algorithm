import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))

    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    result = numbers[-1] - numbers[0]
    print('#{} {}'.format(tc+1, result))
