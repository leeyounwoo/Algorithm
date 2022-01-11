import sys
sys.stdin = open('input.txt')


def quick_sort(arr, left, right):
    if left >= right:
        return
    if left < right:
        pivot = partition(arr, left, right)
        quick_sort(arr, left, pivot - 1)
        quick_sort(arr, pivot + 1, right)


def partition(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end
    while left <= right:
        while (left <= right and arr[left] <= pivot):
            left += 1
        while (left <= right and arr[right] >= pivot):
            right -= 1
        if (left <= right):
            arr[left], arr[right] = arr[right], arr[left]
    arr[start], arr[right] = arr[right], arr[start]
    return right


for T in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    quick_sort(arr, 0, len(arr) - 1)
    print("#{} {}".format(T, arr[N // 2]))