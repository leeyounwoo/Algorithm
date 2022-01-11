def selection_sort(arr):
    for i in range(len(arr)-1):
        min_num = i

        for j in range(i+1, len(arr)):
            if arr[min_num] > arr[j]:
                min_num = j
        arr[i], arr[min_num] = arr[min_num], arr[i]

    return arr


arr = [3, 4, 2, 5, 1]

print(selection_sort(arr))