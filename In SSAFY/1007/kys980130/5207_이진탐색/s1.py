import sys
sys.stdin = open('input.txt')
def binary_search(arr, target):
    flag = 0
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
            if flag == 1:
                break
            flag = 1
        elif arr[mid] < target:
            left = mid + 1
            if flag == -1:
                break
            flag = -1

    return -1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    total = 0
    for i in B:
        if binary_search(A, i) != -1:
            total += 1
    print('#{} {}'.format(tc, total))