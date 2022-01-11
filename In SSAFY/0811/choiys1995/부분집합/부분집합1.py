arr = [1, 2, 3, 4]
n = len(arr)

for i in range(1 << n):#(1 << n) == 2^n
    for j in range(n):
        if i & (1 << j):
            print(arr[j], end=" ")
    print()
