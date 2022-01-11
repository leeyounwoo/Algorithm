import sys
sys.stdin = open('input.txt')

T = int(input())
arr = [i for i in range(1, 13)]

for tc in range(T):
    N, K = map(int, input().split())
    count = 0

    for i in range(1 << 12):

        if bin(i).count('1') != N:
            continue

        total = 0
        for j in range(12):
            if i & (1 << j):
                total += arr[j]

        if total == K:
            count += 1
    print('#{} {}'.format(tc + 1, count))




