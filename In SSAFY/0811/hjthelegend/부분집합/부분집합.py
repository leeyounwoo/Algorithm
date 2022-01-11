arr = [1, 2, 3, 4]
n = len(arr)
# 0001
# 0010
# 0100
# 10000011
# 0110
# 1100
# 0101
# 1001
# ...~
# 1111
for i in range(1 << n):
    for j in range(n):
        if i & (1 << j):
            print(arr[j], end=' ')
    print()
