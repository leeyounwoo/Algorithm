arr = [1, 2, 3, 4]

len_num = len(arr)

for i in range(1 << len_num):
    for j in range(len_num):
        if i & (1 << j):
            print(arr[j], end=' ')
    print()