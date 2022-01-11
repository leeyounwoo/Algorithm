def quicksort(arr, start, end):
    pivot = arr[end]
    store_index = start

    for i in range(start, end):
        if arr[i] <= pivot:
            arr[i], arr[store_index]