import sys
sys.stdin = open('input.txt')

T = int(input())
arr = [i for i in range(1, 13)]

for tc in range(T):
    N, K = map(int, input().split())
    n = len(arr)
    count = 0

    for i in range(1<<n):
        total = 0
        new_arr = []
        for j in range(n):
            if i & (1<<j):
                total += arr[j]
                new_arr.append(arr[j])

        if total == K and len(new_arr) == N:
            count += 1
    print("#{} {}".format(tc+1, count))