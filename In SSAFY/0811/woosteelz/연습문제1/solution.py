arr = [-1, 5, 10, 7, -5, 9, 2, 3, 0, 15]
n = len(arr)

for i in range(1 << n):
    temp = []
    for j in range(n):
        if i & (1 << j):
            temp.append(arr[j])
    if sum(temp) == 0:
        print(temp)