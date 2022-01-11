import sys
sys.stdin = open("input.txt")
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    numbers = list(range(1, 13))
    count = 0
    for i in range(1 << 12):
        total = 0
        result = []
        for j in range(12):
            if i & (1 << j):
                result.append(numbers[j])
                total += numbers[j]
        if len(result) == N and total == K:
            count += 1
    print('#{} {}'.format(tc, count))

