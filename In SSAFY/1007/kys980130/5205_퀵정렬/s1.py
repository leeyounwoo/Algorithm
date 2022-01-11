import sys
sys.stdin = open('input.txt')
def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]
    less = []
    equal = []
    more = []

    for num in arr:
        if num < pivot:
            less.append(num)
        elif num == pivot:
            equal.append(num)
        elif num > pivot:
            more.append(num)

    return quicksort(less) + equal + quicksort(more)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    numbers = quicksort(numbers)
    print('#{} {}'.format(tc, numbers[N//2]))