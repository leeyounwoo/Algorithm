import sys
sys.stdin = open('input.txt')


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    # 오른쪽: 1, 왼쪽: -1
    prev = 0
    now = 0

    while left <= right:
        if now == 1:
            prev = 1
            now = 0
        if now == -1:
            prev = -1
            now = 0

        mid = (left + right) // 2
        if arr[mid] == target:
            return 1
        # 왼쪽
        elif arr[mid] > target:
            right = mid - 1
            now = -1
            if prev == -1:
                return 0
        # 오른쪽
        elif arr[mid] < target:
            left = mid + 1
            now = 1
            if prev == 1:
                return 0

    return 0


for T in range(1, 1+int(input())):
    N, M = map(int, input().split())
    arr1 = sorted(list(map(int, input().split())))
    arr2 = list(map(int, input().split()))
    cnt = 0
    for i in range(len(arr2)):
        num = arr2[i]
        cnt += binary_search(arr1, num)
    print('#{} {}'.format(T, cnt))
