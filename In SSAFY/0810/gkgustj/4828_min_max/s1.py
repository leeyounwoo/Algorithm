import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1) :
    N = int(input())
    numbers = list(map(int, input().split()))

    for i in range(len(numbers)) :
        for j in range(i-1, -1, -1) :
            if numbers[j] > numbers[j+1] :
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    print(f'#{t} {numbers[-1]-numbers[0]}')