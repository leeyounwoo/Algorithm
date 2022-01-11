import sys
sys.stdin = open("input.txt")
T = int(input())
for tc in range(T):
    N, M = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    max = min = sum(numbers[0:M])

    for i in range(1, N-M+1):
        if max < sum(numbers[i:i+M]):
            max = sum(numbers[i:i+M])
        if min > sum(numbers[i:i+M]):
            min = sum(numbers[i:i+M])
    print('#{} {}'.format(tc+1, max-min))

