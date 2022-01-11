import sys
sys.stdin = open('input.txt')


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    less = []
    equal = []
    more = []

    for num in arr:
        if num < pivot:
            less.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            more.append(num)

    return quick_sort(less) + equal + quick_sort(more)


for T in range(1, 1+int(input())):
    N = int(input())
    arr = list(map(int, input().split()))

    print('#{} {}'.format(T, quick_sort(arr)[N//2]))