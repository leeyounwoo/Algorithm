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


arr = [5, 3, 7, 7, 7, 1, 4]
print(quick_sort(arr))
