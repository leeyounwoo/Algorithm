def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_num = i
        for j in range(i+1, len(arr)):
            if arr[min_num] > arr[j]:
                min_num = j
        arr[min_num], arr[i] = arr[i], arr[min_num]
    return arr

arr = [51, 8, 25, 13, 28]

print(selection_sort(arr))