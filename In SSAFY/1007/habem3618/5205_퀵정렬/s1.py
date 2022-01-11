import sys
sys.stdin = open('input.txt')


def partition(arr, start, end):
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while arr[left] <= arr[pivot] and left <= end:
            left += 1

        while arr[right] >= arr[pivot] and start < right:
            right -= 1

        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]

    return right


def quick_sort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        if pivot == N // 2:
            return
        elif pivot > N // 2:
            quick_sort(arr, start, pivot - 1)
        else:
            quick_sort(arr, pivot + 1, end)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, N-1)
    # print(arr)
    print('#{} {}'.format(tc, arr[N//2]))
