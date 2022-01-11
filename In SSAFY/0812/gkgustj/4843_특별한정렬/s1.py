import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    # 최소값 찾기
    for i in range(len(numbers)-1):
        min_idx = i

        for j in range(i, len(numbers)):
            if numbers[j] < numbers[min_idx]:
                min_idx = j

        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

    result = []
    for _ in range(5):
        result.append(numbers.pop())
        result.append(numbers.pop(0))

    print('#{}'.format(t), end=' ')
    print(*result)