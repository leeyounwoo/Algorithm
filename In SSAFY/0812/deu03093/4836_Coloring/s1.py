import sys

sys.stdin = open('input.txt')

for T in range(1, int(input()) + 1):
    arr = [[0] * 10 for _ in range(10)]
    n = int(input())
    for _ in range(n):
        i1, j1, i2, j2, color = map(int, input().split())
        for i in range(i1, i2 + 1):
            for j in range(j1, j2 + 1):
                arr[i][j] += color
    ans = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 3:
                ans += 1

    print('#{} {}'.format(T, ans))