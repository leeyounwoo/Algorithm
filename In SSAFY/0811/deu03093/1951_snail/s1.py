import sys

sys.stdin = open('input.txt')

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
for T in range(1, int(input()) + 1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]
    count = 1
    now_i = 0
    now_j = 0
    if n == 1:
        arr = [[1]]
    else:
        if n % 2:
            N = n // 2 + 1
        else:
            N = n // 2
        # print(T, N)
        flag = 0
        for cir in range(N):
            while now_j <= n - cir - 1:
                # print(now_i, now_j, count, cir)
                arr[now_i][now_j] = count
                count += 1
                if now_j == n - cir - 1:
                    now_i += 1
                    break
                now_j += 1
            if count == n ** 2 + 1:
                break

            while now_i <= n - cir - 1:
                # print(now_i, now_j, count, cir)
                arr[now_i][now_j] = count
                count += 1
                if now_i == n - cir - 1:
                    now_j -= 1
                    break
                now_i += 1

            while now_j >= cir :
                # print(now_i, now_j, count)
                arr[now_i][now_j] = count
                count += 1
                if now_j == cir:
                    now_i -= 1
                    break
                now_j -= 1

            while now_i >= cir + 1:
                # print(now_i, now_j, count)
                arr[now_i][now_j] = count
                count += 1
                if now_i == cir + 1:
                    now_j += 1
                    break
                now_i -= 1

    print('#{}'.format(T),)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print('{}'.format(arr[i][j]), end=' ')
        print()

