arr = [1, 2, 3, 4]
n = len(arr)

# << : 옮기는 행위
for i in range(1 << n):
    for j in range(n):
        if i & (1 << j):
            print(arr[j], end=" ")
    print()