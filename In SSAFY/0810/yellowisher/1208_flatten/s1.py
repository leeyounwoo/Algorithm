import sys
sys.stdin = open('input.txt')

for T in range(10):
    N = int(input())
    arr = list(map(int, input().split()))
    count = 0

    for i in range(N):
        max_num = 1
        min_num = 100
        for j in range(100):
            if arr[j] > max_num:
                max_num = arr[j]
                max_idx = j
            if arr[j] < min_num:
                min_num = arr[j]
                min_idx = j

        arr[max_idx] -= 1
        arr[min_idx] += 1
        if arr[max_idx] == arr[min_idx]:
            print("#{} {}".format(T + 1, arr[max_num]-arr[min_num]))
            count += 1
            break

    max_num1 = 1
    min_num1 = 100
    for k in range(100):
        if arr[k] > max_num1:
            max_num1 = arr[k]

        if arr[k] < min_num1:
            min_num1 = arr[k]
    if count == 0:
        print("#{} {}".format(T + 1, max_num1-min_num1))