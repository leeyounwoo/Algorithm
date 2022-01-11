arr = [-1, 5, 10, 7, -5, 9, 2, 3, 0, 15]
n = len(arr)

for i in range(1 << n):
    total = 0
    for j in range(n):
        if i & (1 << j):
            total += arr[j]
    if total == 0:
        print('0이 되는 경우가 있습니다!')
