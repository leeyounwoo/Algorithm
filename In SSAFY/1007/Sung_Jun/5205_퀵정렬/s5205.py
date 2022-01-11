import sys
sys.stdin = open('input.txt')


# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#
#     pivot = arr[len(arr) // 2]
#     less = []
#     equal = []
#     more = []
#
#     for num in arr:
#         if num < pivot:
#             less.append(num)
#         elif num == pivot:
#             equal.append(num)
#         else:
#             more.append(num)
#
#     return quick_sort(less) + equal + quick_sort(more)


def partition(arr, start, end):
    pivot = arr[end]
    left = start
    right = end - 1
    while left <= right:
        while arr[left] <= pivot:
            left += 1
            if left > right:
                break
        while arr[right] >= pivot:
            right -= 1
            if left > right:
                break
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
    arr[left], arr[end] = arr[end], arr[left]
    return left


def quick_sort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quick_sort(arr, start, pivot - 1)
        quick_sort(arr, pivot + 1, end)


T = int(input())
for tc in range(T):
    num = int(input())
    case = list(map(int, input().split()))
    quick_sort(case, 0, len(case)-1)
    print('#{} {}'.format(tc+1, case[num//2]))
    # print('#{} {}'.format(tc+1, quick_sort(case)[num//2]))
