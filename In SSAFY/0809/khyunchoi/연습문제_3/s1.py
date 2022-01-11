import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    max_diff = 0
    for i in range(N):
        cnt = 0
        for j in range(i+1, N):
            if arr[i] <= arr[j]:
                cnt += 1
        diff = (N - i - 1) - cnt

        if max_diff < diff:
            max_diff = diff

    print(max_diff)