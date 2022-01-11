arr = [1, 2, 3, 4]
n = len(arr)

for i in range(1 << n): #집합에서 1개만 뽑는경우, 2개만뽑는경우...
    for j in range(n):
        if i & (1 << j):
            print(arr[j], end=" ")
    print()
