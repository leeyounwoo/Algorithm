import sys
sys.stdin = open('input.txt')


def binary_search(arr, target):
    global result

    left = 0
    right = len(arr) - 1

    mid = (left + right) // 2

    if arr[mid] == target:
        result += 1
        return
    elif arr[mid] > target:
        right = mid - 1
        is_left = True
    elif arr[mid] < target:
        left = mid + 1
        is_left = False

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            result += 1
            return
        elif arr[mid] > target:
            if is_left:
                return
            right = mid - 1
            is_left = True
        elif arr[mid] < target:
            if not is_left:
                return
            left = mid + 1
            is_left = False


T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())
    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))
    A_list.sort()

    result = 0
    for num in B_list:
        binary_search(A_list, num)

    print('#{} {}'.format(tc, result))