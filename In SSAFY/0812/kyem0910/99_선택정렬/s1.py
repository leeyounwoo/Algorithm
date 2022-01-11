arr = [64, 25, 10, 22, 11]

for i in range(len(arr) - 1):
    index_min = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[index_min]:
            index_min = j
    arr[index_min], arr[i] = arr[i], arr[index_min]

print(arr)