n = len(arr)
arr = list(map(int, input().split()))
for i in range(1<<n):
    total = 0
    for j in range(n):
        if i & (1<<j):
            total += arr[j]
    if total == 0:
        print('0 존재')
        break