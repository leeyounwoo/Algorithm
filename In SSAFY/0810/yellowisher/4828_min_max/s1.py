import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    max_number = arr[0]
    min_number = arr[0]

    for i in range(1, N):
        if arr[i] > max_number:
            max_number = arr[i]

    for i in range(1, N):
        if arr[i] < min_number:
            min_number = arr[i]

    print("#{} {}".format(test_case + 1, max_number - min_number))