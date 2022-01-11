
arr = [3, 2, 1]
n = len(arr)

for i in range(n):
    minimun = i
    for j in range(i+1, n):
        if arr[minimum] > arr[j]:
            minimum = j
    arr[minimum], arr[i] = arr[i], arr[minimum]