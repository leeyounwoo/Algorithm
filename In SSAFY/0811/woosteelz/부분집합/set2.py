arr = [1, 2, 3, 4]
arr_part = [[], [1], [2], [3], [4],
            [1, 2], [1, 3], [1, 4],
            [2, 3], [2, 4],
            [3, 4],
            [1, 2, 3], [1, 2, 4], [1, 3, 4],
            [2, 3, 4],
            [1, 2, 3, 4]]
arr_set = []
n = len(arr)
for i in range(1 << n):
    temp = []
    for j in range(n):
        if i & (1 << j):
            temp.append(arr[j])
    arr_set.append(temp)

print(arr_set)