import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    prefix = list(map(int, input().split()))

    prefix_min = 0
    for i in range(M):
        prefix_min += prefix[i]

    prefix_max = prefix_min

    for i in range(1, N - M + 1):
        prefix_sum = 0
        for j in range(i, i + M):
            prefix_sum += prefix[j]
        if prefix_sum > prefix_max:
            prefix_max = prefix_sum
        if prefix_sum < prefix_min:
            prefix_min = prefix_sum

    print(prefix_max - prefix_min)

